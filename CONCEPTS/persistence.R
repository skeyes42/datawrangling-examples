library(S7)


StatLine <- new_class("StatLine",
  properties = list(
    FGM = class_integer,
    FGA = class_integer,
    FG3M = class_integer,
    FG3A = class_integer,
    FTM = class_integer,
    FTA = class_integer
  )
)

stat1 = StatLine(
  FGM = 10L,
  FGA = 20L,
  FG3M = 3L,
  FG3A = 8L,
  FTM = 5L,
  FTA = 6L
)

print('--- StatLine Instance ---')
print(stat1)

# Save
saveRDS(stat1, "stat1.rds")

# Remove from environment
rm(stat1)

# Load
stat1 <- readRDS("stat1.rds")

print('--- Loaded StatLine Instance ---')
print(stat1)

