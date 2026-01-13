## class_example.R

This program demonstrates the use of the **S7 package**, which is the successor to R’s older S3 and S4 object-oriented systems. It provides a formal, modern way to define classes, properties, and methods in R.

Here is a breakdown of the components:

**1. Data Preparation**

The program uses tibble::tribble() to create a small basketball dataset. This format is "row-wise," making it easy to read the Game, Team, and Player stats for field goals (FGM), three-pointers (FG3M), and free throws (FTM).

**2. Class Definition (new_class)**

The Boxscore \<- new_class(...) block defines a new object type:

Properties: It defines one property, data, and enforces that it must be a class_data.frame.

Validator: This is a safety check. When you create a Boxscore object, the validator ensures the provided data frame contains all six required basketball columns. If any are missing, it returns an error message.

**3. Custom Method Definition (method)**

In R, print is a "generic" function. This program registers a specific version of print specifically for the Boxscore class:

Logic: Instead of just showing the table, it calculates summary metadata (total rows and unique games).

Formatting: It prints a custom header (e.g., Boxscore: 8 rows, 2 games) before displaying the actual data.

invisible(x): This is a standard R practice for print methods, allowing the object to be returned silently if assigned to a variable.

**4. Main Program Execution**

Instantiation: box \<- Boxscore(data = df) creates a new instance of the Boxscore class. During this step, S7 automatically runs the validator to ensure df is valid.

Dispatch: When print(box) is called, R’s method dispatch system looks at the class of box. Because it is an S7 Boxscore object, it executes the custom print method defined earlier.

**Why use this approach?**

By using S7, you move away from "loose" data frames and toward Type Safety. If you accidentally tried to create a Boxscore with a data frame missing the GAME_ID column, the program would stop immediately with a clear error, preventing bugs in downstream analysis.
