**Step 1 - Define CSV data in Python**

python

boxscores_data = """

GAME_ID,PLAYER_ID,FGM,FGA,FG3M,FG3A

1000,1,10,13,12,13

...

"""

Just a raw CSV string sitting in Python memory. No files written, no database — pure in-memory data.

**Step 2 - Connect to Rserve and push the data to R**

python

conn = connect(host='localhost', port=6311)

conn.r.boxscores_csv = boxscores_data

This connects to the running R server, then uses conn.r to inject the Python string directly into R's environment as a variable called boxscores_csv. R can now see and use this data.

**Step 3 - Execute R code for data transformation**

python

r_code = """

library(dplyr)

df \<- read.csv(text = boxscores_csv, stringsAsFactors = FALSE)

result \<- df %\>%

group_by(PLAYER_ID) %\>%

summarize(avg_FGM = mean(FGM), avg_FG3M = mean(FG3M))

result

"""

result = conn.eval(r_code)

This sends a multi-line block of R code to be executed on the server. The R code:

-   Loads the dplyr library
-   Reads the CSV string (sent from Python) into an R dataframe using read.csv(text = ...)
-   Uses dplyr pipe syntax to group by player and calculate averages
-   Returns result back to Python

The last line result in the R code is critical — whatever that evaluates to is what gets returned to Python. In this case, it's an R dataframe that comes back as a TaggedList.

**Step 4 - Convert TaggedList to pandas DataFrame**

python

df = pd.DataFrame({

'PLAYER_ID': list(result['PLAYER_ID']),

'avg_FGM': list(result['avg_FGM']),

'avg_FG3M': list(result['avg_FG3M'])

})

This is a **hardcoded column-by-column conversion**. The programmer knows the R code will return exactly three columns (PLAYER_ID, avg_FGM, avg_FG3M), so they manually extract each one from the TaggedList by name and wrap it in a dictionary for pandas.

**Note:** This is less flexible than your earlier program's approach using result_df.keys and result_df.values with a loop, which works for any number of columns. The approach here only works if you know the exact column names ahead of time.

**Step 5 - Execute a follow-up R query**

python

total_games = conn.eval('length(unique(df\$GAME_ID))')

This demonstrates that R's environment is **stateful**. The df variable created in Step 3 is still alive in R's memory, so you can query it again without re-sending the data. This is powerful for iterative analysis — Python can keep asking R questions about the same dataset without repeated data transfers.

**Step 6 - Clean up**

python

conn.close()

\`\`\`

Closes the connection to the R server. Important for production code to avoid leaving connections open.
