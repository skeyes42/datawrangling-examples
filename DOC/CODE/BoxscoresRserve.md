**What it does overall:** It connects to a running R server (Rserve), asks R to query the Boxscores database using the R class we've seen in earlier examples, and brings the results back to Python as a pandas DataFrame for analysis.

**Step 1 - Resolve paths**

python

examples\_dir = os.getenv("EXAMPLES")

db\_path = os.path.join(examples\_dir, "Boxscores.db")

r\_class\_path = os.path.join(examples\_dir, "LIBRARY", "BoxscoresClass.R")

r\_class\_path = r\_class\_path.replace("\\\\", "/")

Gets the database and R class file locations from the EXAMPLES environment variable. The backslash-to-forward-slash conversion is necessary because Windows paths with backslashes cause R to throw escape sequence errors when the path is passed as a string.

**Step 2 - Connect to Rserve**

python

conn = connect(host="localhost", port=6311)

Unlike RPY2 which embeds R inside Python, Rserve runs as a **separate server process**. Python connects to it over a network socket, just like connecting to a database. R must already be running with Rserve() called before this line executes.

**Step 3 - Push the DB path into R and load the R class**

python

conn.r.db\_path = db\_path

conn.eval(f'source("{r\_class\_path}")')

Two things happen here. First, conn.r.db\_path = db\_path pushes the database path from Python directly into R's environment as a variable. Second, source() tells R to load and parse BoxscoresClass.R, making the get\_Boxscores\_data() function available in R's environment.

**Step 4 - Call the R function**

python

result\_df = conn.eval("get\_Boxscores\_data()")

This tells R to execute get\_Boxscores\_data(), which connects to the SQLite database, runs the joins across the Boxscores, Players, and Teams tables, and returns the result. The data comes back to Python as a TaggedList object — pyRserve's representation of an R dataframe.

**Step 5 - Convert TaggedList to pandas DataFrame**

python

data = {}

for i in range(len(result\_df.keys)):

col\_name = result\_df.keys\[i]

col\_data = result\_df.values\[i]

data\[col\_name] = col\_data

df = pd.DataFrame(data)

This is the most technically interesting part, and the result of some debugging work. Unlike RPY2 which converts R dataframes to pandas automatically, pyRserve returns a TaggedList which requires manual conversion. The TaggedList has two parallel attributes — keys (column names) and values (column data as numpy arrays) — both accessed by integer index. The loop pairs them up into a plain Python dictionary, which pandas can then convert to a DataFrame cleanly.

**Step 6 - Analyze the data in Python**

python

df\[numeric\_cols].describe()

high\_scorers = df\[df\["FGM"] > 8]

```

Once converted to a pandas DataFrame, standard Python data analysis takes over — summary statistics, filtering, and so on. R's job is done at this point.




