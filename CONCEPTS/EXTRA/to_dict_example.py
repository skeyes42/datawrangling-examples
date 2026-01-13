import pandas as pd
from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int
    city: str

# Say you have this DataFrame:
columns = ['name', 'age', 'city']    # Columns
data =    [
          ['Alice', 25,    'NYC'],   # Row 0
          ['Bob',   30,    'LA' ]    # Row 1
]

df = pd.DataFrame(data, columns=columns)

# to_dict('records') converts it to a list of dictionaries:
records = df.to_dict('records')
# Result:
# [
#   {'name': 'Alice', 'age': 25, 'city': 'NYC'},
#   {'name': 'Bob', 'age': 30, 'city': 'LA'}
# ]
print('--- records ---')
print(records)
print('\n')

people = [Person(**row) for row in records]

print('--- Persons ---')
for person in people:
    print(person)


