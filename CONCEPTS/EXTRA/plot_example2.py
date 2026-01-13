import pandas as pd
import matplotlib.pyplot as plt

# 1. Create the data (equivalent to tibble::tribble)
data = {
    'GAME_ID': [1000, 1000, 1000, 1000, 2000, 2000, 2000, 2000],
    'TEAM_ID': [100, 100, 200, 200, 100, 100, 300, 300],
    'PLAYER_ID': [1, 2, 3, 4, 1, 2, 5, 6],
    'FGM': [10, 4, 2, 8, 10, 11, 8, 7],
    'FG3M': [12, 4, 6, 2, 4, 5, 10, 6],
    'FTM': [12, 7, 5, 7, 10, 4, 9, 3]
}
df = pd.DataFrame(data)

# 2. Reshape the data (equivalent to pivot_longer)
# We use melt to turn columns into rows
df_long = df.melt(
    id_vars=['GAME_ID', 'TEAM_ID', 'PLAYER_ID'], 
    value_vars=['FGM', 'FG3M', 'FTM'],
    var_name='stat_type', 
    value_name='value'
)

# Equivalent to print(my_data_long, n = Inf)
print(df_long.to_string())

# 3. Create the grouped bar chart
# In Python, it is often easier to pivot for plotting or use the 'hue' concept
plot_df = df_long.groupby(['PLAYER_ID', 'stat_type'])['value'].sum().unstack()

ax = plot_df.plot(kind='bar', figsize=(6, 3), width=0.8)

# 4. Styling (equivalent to labs and theme_minimal)
plt.title("Player Statistics by Type")
plt.xlabel("Player ID")
plt.ylabel("Count")
plt.legend(title="Statistic")
plt.xticks(rotation=0) # Keep Player IDs horizontal
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()

# 5. Save the plot (equivalent to ggsave)
plt.savefig("my_plot_grouped.png")

# Show the plot
plt.show()
