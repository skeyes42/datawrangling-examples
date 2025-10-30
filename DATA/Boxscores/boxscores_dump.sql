/* Direct output to file */
.output "results.csv"

/* Set format of output to csv */
.mode csv

/* Move header column names to output */
.header on

/* Get all Boxscores table rows to output */
SELECT * FROM Boxscores;

/* Close ouptut */
.output stdout
