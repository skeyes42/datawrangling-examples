import pandas as pd
# Create a sample data frame
df = pd.DataFrame({
    'id': [1, 2, 3],
    'value1': [10, 20, 30],
    'value2': [2, 5, 3]
})
# Use assign() with a lambda function to create a new column
df_modified = df.assign(
    new_value=lambda x: x['value1'] * 2 + x['value2']
)
# Print the modified data frame
print(df_modified)