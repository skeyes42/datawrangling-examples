import pandas as pd

# Create the DataFrame
data = {
    'GAME_ID': [1000, 1000, 1000, 1000, 2000, 2000, 2000, 2000],
    'TEAM_ID': [100, 100, 200, 200, 100, 100, 300, 300],
    'PLAYER_ID': [1, 2, 3, 4, 1, 2, 5, 6],
    'FGM': [10, 4, 2, 8, 10, 11, 8, 7],
    'FG3M': [12, 4, 6, 2, 4, 5, 10, 6],
    'FTM': [12, 7, 5, 7, 10, 4, 9, 3]
}
df = pd.DataFrame(data)

print('--- 1 --- # Selecting a single column as a DataFrame')
a = df[['GAME_ID']] 
print(type(a))
print(a)

print('\n--- 2 --- # Selecting a specific scalar value')
b = df.iloc[0, 0]
print(type(b))
print(b)

print('\n--- 3 --- # Selecting a single row')
c = df.iloc[[0]]
print(type(c))
print(c)

print('\n--- 4 --- # Selecting a single column as a Series')
d = df.iloc[:, 0]
print(type(d))
print(d)

print('\n--- 5 --- # Extracting column values (equivalent to [[1]])')
x = df['GAME_ID']
print(type(x))
print(x)
