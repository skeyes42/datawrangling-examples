import pandas as pd
# Create a sample data frame
df = pd.DataFrame({
    'id': [1, 2, 3],
    'value1': [10, 20, 30],
    'value2': [2, 5, 3]
})
# Use an anonymous function (lambda) with apply () to create a new column
# axis=1 ensures the function operates on rows
df['new_value'] = df.apply(lambda row: row['value1'] * 2 + row['value2'], axis=1)
# Print the modified data frame
print(df)