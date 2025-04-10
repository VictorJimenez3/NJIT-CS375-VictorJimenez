# NJIT-CS375-[Victor Jimenez]

This dataset contains statistics for NBA players from the 2023 season. It originally includes over 400 records, one for each player. To make the dataset more meaningful, players who averaged fewer than 15 minutes per game were filtered out, leaving a more focused group of contributors. The cleaned data includes player performance stats in per-game format.

Some of the key features in the dataset include points, assists, rebounds, field goal percentage, three-point percentage, minutes per game, turnovers, steals, blocks, games played, and plus/minus. The dataset also includes a new binary column, `is_all_star`, which indicates whether a player was selected as a 2023 NBA All-Star.

Link to Dataset: https://www.kaggle.com/datasets/amirhosseinmirzaie/nba-players-stats2023-season  
Link to Preprocessing Code: in cs_375_project_victor_jimenez.ipynb

## Classification Problem

Predict whether a player will be selected as an NBA All-Star using regular season statistics.  
Input features: minutes per game, points per game, assists, rebounds, field goal percentage, three-point percentage, turnovers, steals, blocks, games played, and plus/minus  
Target variable: is_all_star (1 for All-Star, 0 for non-All-Star)  
Challenges: The class is highly imbalanced since only a small percentage of players are selected. Additionally, fan/media voting can introduce bias that is not reflected in player performance.  
Real world application: This model could help with scouting, identifying under-the-radar players, or improving fantasy basketball recommendations.

## Regression Problem

Predict a player’s points per game (PPG) for the next season based on current stats.  
Input features: current points, assists, rebounds, FG%, 3PT%, PER, minutes per game, age, team  
Target variable: next_season_ppg  
Challenges: Player injuries, trades, and role changes are difficult to account for and can affect accuracy.  
Real world application: This type of model could be used to forecast performance, assist fantasy team managers, or support player development analysis.

## Why I Chose This Dataset

I follow the NBA closely and have always been interested in what goes into All-Star selections. Every season, there are debates around snubs and surprises. This dataset gives me a chance to explore whether stats alone can explain those decisions. The data is rich, clean, and offers a lot of potential for both classification and regression tasks.

## Ethical Considerations

The All-Star selection process includes subjective elements like fan voting and media attention, which may introduce bias into the target label. However, the dataset itself contains only publicly available performance data, and does not include any private or sensitive information about the players.
