import pickle
from dataclasses import dataclass

@dataclass
class StatLine:
    FGM: int
    FGA: int
    FG3M: int
    FG3A: int
    FTM: int
    FTA: int
    
stat1 = StatLine(
    FGM=10, 
    FGA=25, 
    FG3M=4, 
    FG3A=10, 
    FTM=5, 
    FTA=6
)

print('--- StatLine Object ---')
print(stat1)

# Save
with open('stat1.pkl', 'wb') as f:
    pickle.dump(stat1, f)

del stat1  # Remove from memory

# Load stat1
with open('stat1.pkl', 'rb') as f:
   stat1 = pickle.load(f)

print('--- Loaded StatLine Object ---')
print(stat1)