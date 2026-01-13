import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sys

# Starting data
data = {
    'GAME_ID': [1000, 1000, 1000, 1000, 2000, 2000, 2000, 2000],
    'TEAM_ID': [100, 100, 200, 200, 100, 100, 300, 300],
    'PLAYER_ID': [1, 2, 3, 4, 1, 2, 5, 6],
    'FGM': [10, 4, 2, 8, 10, 11, 8, 7],
    'FG3M': [12, 4, 6, 2, 4, 5, 10, 6],
    'FTM': [12, 7, 5, 7, 10, 4, 9, 3]
}
df = pd.DataFrame(data)

# ===== PIVOT_WIDER (Reshaping to wide format) =====
player_across_games = df.pivot(
    index='PLAYER_ID', 
    columns='GAME_ID', 
    values=['FGM', 'FG3M', 'FTM']
)

# Flatten multi-index columns to match R's "FGM_game1000" style
player_across_games.columns = [f"{stat}_game{int(game)}" for stat, game in player_across_games.columns]
player_across_games = player_across_games.reset_index()

# Calculate deltas
player_across_games['FGM_change'] = player_across_games['FGM_game2000'] - player_across_games['FGM_game1000']
player_across_games['FG3M_change'] = player_across_games['FG3M_game2000'] - player_across_games['FG3M_game1000']

# ===== PIVOT_LONGER (Melting) =====
player_stat_breakdown = df.melt(
    id_vars=['GAME_ID', 'TEAM_ID', 'PLAYER_ID'],
    value_vars=['FGM', 'FG3M', 'FTM'],
    var_name='stat_type',
    value_name='value'
)

# Summarize stats
player_analysis_stats = player_stat_breakdown.groupby(['PLAYER_ID', 'stat_type'])['value'].agg(
    avg_value='mean',
    total_value='sum'
).reset_index().sort_values(['PLAYER_ID', 'avg_value'], ascending=[True, False])

# Find each player's strongest stat per game (slice_max equivalent)
idx = player_stat_breakdown.groupby(['GAME_ID', 'PLAYER_ID'])['value'].idxmax()
player_strongest = player_stat_breakdown.loc[idx]

sns.set_theme(style="whitegrid")

g = sns.FacetGrid(player_stat_breakdown, row="PLAYER_ID", col="GAME_ID", margin_titles=True)
g.map_dataframe(sns.barplot, x="stat_type", y="value", palette="gray", hue="stat_type", legend=False)

g.set_axis_labels("Stat Type", "Value")
g.set_titles(row_template="Player: {row_name}", col_template="Game: {col_name}")
plt.subplots_adjust(top=0.9)
g.fig.suptitle("Player Performance Breakdown by Game")

for ax in g.axes.flat:
    for label in ax.get_xticklabels():
        label.set_rotation(45)

plt.savefig("faceted_bar_chart.png", dpi=300)
plt.show()