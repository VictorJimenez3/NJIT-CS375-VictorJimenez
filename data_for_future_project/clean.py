import pandas as pd
from pathlib import Path

# 1) Define paths
base = Path(__file__).parent
stats_fp  = base / 'Seasons_Stats_cleaned.csv'
labels_fp = base / 'all_nba_correct.csv'
out_fp    = base / 'data_used_for_models.csv'

# 2) Load your two source files
stats  = pd.read_csv(stats_fp)
labels = pd.read_csv(labels_fp)

# 3) Merge on Year, Player, Position
df = stats.merge(labels, on=['Year','Player','Position'], how='left')

# 4) Create the nba_team column, filling missing with 'None'
df['nba_team'] = df['Team'].fillna('None')

# 5) (Optional) Drop the original Team column if you like
df = df.drop(columns=['Team'])

# 6) Print a sample to verify
print("=== Sample of merged data ===")
print(df[['Year','Player','Position','nba_team']].head(10))

# 7) Save the combined CSV
df.to_csv(out_fp, index=False)
print(f"\nSaved merged dataset (with nba_team) to {out_fp}")
