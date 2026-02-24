# Side-by-Side R and Python Data Wrangling Examples

Working code repository for *Side-by-Side R and Python Data Wrangling using SQLite3, Reticulate, RPY2 and Rserve with OO* 
by Steve Keyes. Every example in the book has a corresponding R and Python 
implementation here.

Related: [Using Python OOP to Analyze NBA Boxscore Data](https://medium.com/@skeyes42/using-python-oop-to-analyze-nba-boxscore-data-be313120bd18) 
| [Article repo](https://github.com/skeyes42/OOviewBoxscoreData)

---

## What's in this repo

All examples run against a shared SQLite database (Boxscores.db) built from 
simplified NBA boxscore data — 3 teams, 2 players per team, 3 games per season. 
Small enough to see every transformation clearly, realistic enough to matter.
```
datawrangling-examples/
│
├── code/
│   ├── concepts/          ← R and Python code for Foundations chapters (3–10)
│   └── examples/          ← R and Python code for Applied chapters (12–25)
│
├── data/
│   └── boxscores/
│       ├── csv/           ← CSV files for loading database tables
│       ├── sql/           ← SQL scripts for database setup and manipulation
│       └── library/       ← Boxscores, Players, Teams & Season class definitions
│
└── doc/                   ← Markdown documentation for all examples
```

The database lives at:
```
datawrangling-examples/data/boxscores/Boxscores.db
```

---

## Setup

### Prerequisites
- R (from [CRAN](https://cran.r-project.org/))
- Python 3.x (from [python.org](https://www.python.org/))
- Git

### Step 1 — Clone the repo
```bash
git clone https://github.com/skeyes42/datawrangling-examples.git
cd datawrangling-examples
```

### Step 2 — Install R packages
```r
# Data manipulation
install.packages("dplyr")
install.packages("tidyverse")
install.packages("readr")
install.packages("stringr")
install.packages("janitor")
install.packages("purrr")

# Database
install.packages("DBI")
install.packages("RSQLite")
install.packages("dbplyr")

# Visualization
install.packages("ggplot2")
install.packages("ggpattern")
install.packages("rhandsontable")

# Cross-language interoperability
install.packages("reticulate")
install.packages("Rserve")

# Object-oriented programming
install.packages("S7")
```

### Step 3 — Install Python libraries
```bash
# Core
pip install pandas numpy matplotlib seaborn

# Cross-language interoperability
pip install rpy2 pyRserve

# Utilities
pip install attrs pandastable nba_api plotnine
```

### Step 4 — Set environment variable

Set the `EXAMPLES` environment variable to the root of the cloned repo.

**Windows (PowerShell):**
```powershell
[Environment]::SetEnvironmentVariable("EXAMPLES", "C:\path\to\datawrangling-examples", "User")
```

**Linux/Mac:**
```bash
echo 'export EXAMPLES="/path/to/datawrangling-examples"' >> ~/.bashrc
source ~/.bashrc
```

### Step 5 — Load the database
```bash
cd data/boxscores/sql
sqlite3 ../Boxscores.db < create_boxscores.sql
```

---

## Verify your setup

**R:**
```r
library(DBI)
library(RSQLite)

con <- dbConnect(RSQLite::SQLite(), 
                 file.path(Sys.getenv("EXAMPLES"), 
                 "data/boxscores/Boxscores.db"))
dbListTables(con)
# Should return: Boxscores, Players, Teams, Season2025
dbDisconnect(con)
```

**Python:**
```python
import sqlite3
import os

db_path = os.path.join(os.environ["EXAMPLES"], "data/boxscores/Boxscores.db")
con = sqlite3.connect(db_path)
cursor = con.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
print(cursor.fetchall())
# Should return: [('Boxscores',), ('Players',), ('Teams',), ('Season2025',)]
con.close()
```

If both return the four table names, you're ready to go.

---

## Where to start

If you're new to the repo, start with the Foundations chapters:

| Topic | R file | Python file |
|---|---|---|
| Joins and merges | `code/concepts/joins.R` | `code/concepts/joins.py` |
| Chaining | `code/concepts/chaining.R` | `code/concepts/chaining.py` |
| Variable creation | `code/concepts/variables.R` | `code/concepts/variables.py` |
| Summarize/aggregate | `code/concepts/summarize.R` | `code/concepts/summarize.py` |
| Classes | `code/concepts/classes.R` | `code/concepts/classes.py` |

Full documentation for every example is in the `doc/` folder.

---

## Questions or issues

Open a GitHub issue or reach out at skeyes42@gmail.com