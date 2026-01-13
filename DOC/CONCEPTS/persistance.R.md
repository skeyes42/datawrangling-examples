## persistance.R

This program demonstrates how to define a custom data structure using R's **S7 object-oriented system** and how to perform **object persistence** (saving and loading) using the standard R .rds format.

Here is a breakdown of the code for 2026:

**1. Class Definition (StatLine)**

The program uses new_class() from the S7 package to create a blueprint for basketball statistics.

**Properties**: It defines six specific slots: Field Goals Made/Attempted (FGM/FGA), Three-Pointers (FG3M/FG3A), and Free Throws (FTM/FTA).

**Type Enforcement**: Every property is strictly typed as class_integer. This ensures that you cannot accidentally store a string or a decimal in these fields, preventing data bugs.

**2. Object Instantiation**

The variable stat1 is created as an **instance** of the StatLine class.

Note the use of the L suffix (e.g., 10L). In R, this explicitly denotes an **integer**. Without the L, R treats numbers as "doubles" (decimals), which would cause a type-matching error because the class expects integers.

**3. Object Persistence (Save and Load)**

This is the core functional part of the script:

**saveRDS(stat1, "stat1.rds")**: This serializes the S7 object into a single file on your disk. Unlike a CSV, which only saves raw data, an RDS file saves the **entire object structure**, including its class metadata.

**rm(stat1)**: This command deletes the object from your computer's RAM, proving that the subsequent step is actually loading it from the file.

**readRDS("stat1.rds")**: This restores the object. Because S7 objects are built on top of R's base types, the reloaded stat1 retains its identity as a StatLine object with all its properties intact.

**Key Benefits of this Approach**

**Structure Preservation**: When you reload the data, you don't have to redefine what columns are integers or what the table structure is; the object "remembers" its rules.

**Data Integrity**: By using S7, you ensure that the data being saved to disk has been validated against the class rules before it is ever written.

**Compact Storage**: The .rds format is a compressed binary format, making it much more efficient for storage than a plain text file like a CSV.

For more information on the latest features of S7 in 2026, you can refer to the S7 GitHub repository.
