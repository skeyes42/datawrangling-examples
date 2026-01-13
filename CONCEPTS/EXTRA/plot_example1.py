import pandas as pd
import matplotlib.pyplot as plt

# 1. Create the data
data = {
    "GAME_ID": [1000, 1000, 1000, 1000, 2000, 2000, 2000, 2000],
    "TEAM_ID": [100, 100, 200, 200, 100, 100, 300, 300],
    "PLAYER_ID": [1, 2, 3, 4, 1, 2, 5, 6],
    "FGM": [10, 4, 2, 8, 10, 11, 8, 7],
    "FG3M": [12, 4, 6, 2, 4, 5, 10, 6],
    "FTM": [12, 7, 5, 7, 10, 4, 9, 3]
}
my_data = pd.DataFrame(data)

# 2. Build the plot (Equivalent to geom_bar(stat='identity'))
# Note: Matplotlib bar plots don't automatically sum data for duplicate X values 
# like ggplot's stat="count" does; it behaves like stat="identity" by default.
fig, ax = plt.subplots(figsize=(8, 6))
ax.bar(my_data['PLAYER_ID'], my_data['FGM'])

# Add labels for clarity (ggplot does this automatically)
ax.set_xlabel('PLAYER_ID')
ax.set_ylabel('FGM')

# 3. Save the plot
plt.savefig("my_plot.png")
plt.show()
