# Python: Eager evaluation by default
import pandas as pd
import time

df = pd.DataFrame({
    'GAME_ID': [1000, 1000, 1000, 1000, 2000, 2000, 2000, 2000],
    'TEAM_ID': [100, 100, 200, 200, 100, 100, 300, 300],
    'PLAYER_ID': [1, 2, 3, 4, 1, 2, 5, 6],
    'FGM': [10, 4, 2, 8, 10, 11, 8, 7],
    'FG3M': [12, 4, 6, 2, 4, 5, 10, 6],
    'FTM': [12, 7, 5, 7, 10, 4, 9, 3]
})

# Example 1: Eager evaluation in function arguments
def demonstrate_eager(x, y):
    print("Function called")
    if x > 5:
        print("Returning x, but y was already evaluated")
        return x
    print("Using y")
    return x + y

# This would fail if uncommented - the exception is raised immediately
# result1 = demonstrate_eager(10, ValueError("This errors immediately!"))

# Instead, use lambda for lazy behavior
result1 = demonstrate_eager(10, lambda: ValueError("Never called"))
print(f"Result: {result1}\n")

# Example 2: Pandas evaluates all rows
print("=== Python: assign evaluates all rows ===")
start = time.time()
py_result = df.assign(
    POINTS=lambda d: d.FGM * 2 + d.FG3M * 3 + d.FTM,
    HEAVY_CALC=lambda d: [
        (time.sleep(0.01), p * 2)[1]  # Simulate expensive operation
        for p in d.FGM * 2 + d.FG3M * 3 + d.FTM
    ]
).query('POINTS > 30')
print(f"Time: {time.time() - start:.2f}s")

# Example 3: Groupby operations
print("\n=== Python: Grouped operations ===")
start = time.time()
def expensive_agg(x):
    time.sleep(0.01)
    return x.sum()

team_stats = df.groupby('TEAM_ID').agg(
    total_fgm=('FGM', 'sum'),
    adjusted_score=('FGM', lambda x: expensive_agg(x) * 2 + 
                     df.loc[x.index, 'FG3M'].sum() * 3 + 
                     df.loc[x.index, 'FTM'].sum())
)
print(f"Time: {time.time() - start:.2f}s")
print(team_stats)