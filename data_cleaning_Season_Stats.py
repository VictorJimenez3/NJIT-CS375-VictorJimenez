import pandas as pd

def clean_seasons_stats(input_path: str, output_path: str):
    # 1. Load dataset
    df = pd.read_csv(input_path)

    # 2. Drop unwanted artifact columns
    drop_cols = [c for c in ['Unnamed: 0', 'blanl', 'blank2'] if c in df.columns]
    df.drop(columns=drop_cols, inplace=True)

    # 3. Filter out seasons before 1989
    df = df[df['Year'] >= 1989]

    # 4. Calculate Minutes Per Game (MPG) and filter low-MPG players
    df['MPG'] = df['MP'] / df['G']
    df = df[df['MPG'] >= 15]
    df.drop(columns=['MP'], inplace=True)

    # 5. Create per-game stats and drop raw counts
    per_game_stats = ['PTS', 'AST', 'TRB', 'STL', 'BLK', 'TOV']
    for stat in per_game_stats:
        df[f'{stat}_per_game'] = df[stat] / df['G']
    df.drop(columns=per_game_stats, inplace=True)

    # 6. Group positions into single 'pos' column: Guards (PG, SG) -> G; Forwards (PF, SF) -> F; Centers -> C
    df['pos'] = df['Pos'].replace({'PG': 'G', 'SG': 'G', 'PF': 'F', 'SF': 'F'})
    df.drop(columns=['Pos'], inplace=True)

    # 7. Convert Year to integer
    df['Year'] = df['Year'].astype(int)

    # 8. Select agreed-upon columns
    keep_cols = [
        'Year', 'Player', 'Tm', 'Age', 'G', 'GS', 'MPG',
        'PER','TS%','3PAr','FTr','ORB%','DRB%','TRB%','AST%','STL%','BLK%','TOV%','USG%',
        'eFG%','3P%','2P%','FT%','WS/48','OBPM','DBPM','BPM','VORP',
        'PTS_per_game','AST_per_game','TRB_per_game','STL_per_game','BLK_per_game','TOV_per_game',
        'pos'
    ]
    final_df = df[[col for col in keep_cols if col in df.columns]].copy()

    # 9. Round all floating-point columns to 3 decimals
    float_cols = final_df.select_dtypes(include=['float']).columns
    final_df[float_cols] = final_df[float_cols].round(3)

    # 10. Reset index to start at 1 and use as a numbered index column
    final_df.reset_index(drop=True, inplace=True)
    final_df.index = final_df.index + 1
    final_df.index.name = 'index'

    # 11. Save cleaned DataFrame with numbered index
    final_df.to_csv(output_path, index=True)
    print(f"Cleaned data saved to {output_path}. Columns: {len(final_df.columns)} included.")

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Clean Seasons_Stats dataset')
    parser.add_argument('--input', type=str, default='Seasons_Stats.csv', help='Path to input CSV')
    parser.add_argument('--output', type=str, default='Seasons_Stats_cleaned.csv', help='Path to output cleaned CSV')
    args = parser.parse_args()
    clean_seasons_stats(args.input, args.output)

