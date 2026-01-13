**Project Overview**

**Title:** Side-by-Side R and Python Data Wrangling: Using SQLite3, Reticulate, RPY2 with OO and AI

**Description:**

The purpose of the book is 5-fold:

-   Presentation of foundational topics in the **Foundations** section that explain essential and practical concepts used in defining the “middle” part of the data science workflow: data wrangling (see more detail in the introduction). The goal is not to get lost in an exhaustive attempt to catalog all the features of a particular concept or technology, but rather to provide what’s essential and practical for getting the job done. In other words, the code examples and their comparisons with each other offer **a way** to do things, not **the way**.
-   Presentation of in R and Python (with a common underlying SQLite database infrastructure) that address these data wrangling concepts. The code examples start with a simple, flat set of NBA boxscore-like data and, through the data wrangling process, result in a dataset that ready for exploratory data analysis (EDA) and modeling.
-   From “R versus Python” to “R and Python” working together to leverage their respective strengths, the book presents a discussion of Reticulate and RPY2 technologies at work in R and Python code examples.
-   From a view of boxscore data as flat/relational to a view of boxscore data as object-oriented and hierarchical, the book presents code examples in R and Python using OOP to offer an alternate to what’s being in the analysis of boxscore data. (See my Medium article: “Using Python OOP to Analyze NBA Boxscore Data”.)
-   The moral of the “story” is to leave you equipped to begin his or her own journey in data wrangling.

    **Audience:**

    This book is intended for readers who have some (perhaps limited) experience with R, Python and SQLite. It is not intended to be a tutorial. There are several excellent books on these topics – see References below. For readers learning about data wrangling, the book offers a concise conceptual explanation of basic data wrangling in R and Python using SQLite, as well as practical applications of the concepts in the working code examples. As mentioned above, the book offers “a way” instead of “the way” to understand data wrangling, so for more experienced readers there’s an opportunity to get a fresh look at “how the other guy did it” using individual chapters as reference material.

    **Side-by-side approach:**

    This book presents several examples relevant to data wrangling. For each example, I provide R example code, and equivalent Python code – pointing out similarities and differences between the two. In addition to contrasting R and Python, I provide examples of R and Python co-operating using the reticulate and RPY2 features.

    **Target audience:**

    This book is intended for readers who have some (perhaps limited) experience with R, Python and SQLite. It is not intended to be a tutorial. There are several excellent books on these topics – see References below. For readers learning about data wrangling, the book offers a concise conceptual explanation of basic data wrangling in R and Python using SQLite, as well as practical applications of the concepts in the working code examples. As mentioned above, the book offers “a way” instead of “the way” to understand data wrangling, so for more experienced readers there’s an opportunity to get a fresh look at “how the other guy did it” using individual chapters as reference material.

**About me:**

Steven Keyes (Steve) holds a BS in computer science, and a Master’s degree in data science related studies.

Steve is a retired software developer who worked for SAP on the Document Builder development team. He was responsible for building the database, and for designing and coding the related XSLT transformations. Steve holds two shared patents for Document Builder.

On leaving SAP, Steve created his own consulting company (@Keyes42 Tech) which provided Document Builder consulting services through a certified SAP consulting company.

In addition to his coding and database design experience, he has worked on Python and R projects to do sports analytics using NBA statistics.

**Repository Structure**

**└───datawrangling-examples**

**├───CODE**

**├───EXTRA**

**├───CONCEPTS**

**│ └───EXTRA**

**├───DATA**

**│ └───Boxscores**

**│ └───LIBRARY \_**

**└───DOC**

**├───CODE**

**└───CONCEPTS**

The **CODE** directory contains the main examples – examples that use the full boxscore datasets. These examples are presented and discussed in the **How To** section of the book.

The **CONCEPTS** directory contains shorter examples that are used to present and explain concepts found in the **Foundations** section of the book.

The **DOC** directories contain the markdown files for each example.

**Technical Requirements**

**Here are the R packages required to run the examples:**

\# Core data manipulation packages

install.packages("dplyr")

install.packages("tidyverse")

install.packages("readr")

install.packages("stringr")

install.packages("janitor")

install.packages(“purrr”)

\# Database packages

install.packages("DBI")

install.packages("RSQLite")

install.packages("dbplyr")

\# Visualization packages

install.packages("ggplot2")

install.packages(“ggpattern”)

install.packages("rhandsontable")

\# Cross-language interoperability

install.packages("reticulate")

\# Object-oriented programming

install.packages("S7")

**Here are the Python libraries required to run the examples:**

\# Core data science libraries

pip install pandas numpy matplotlib seaborn

\# Cross-language interoperability

pip install rpy2

\# Database libraries

pip install sqlite

\# Additional utilities

pip install attrs pandastable nba_api plotnine

**Setting up the database:**

Database SQL scripts are in the DATA\\boxscores directory of the repo.

The initial Boxscore.db database can be setup by:

Open a terminal and navigate to:

datawrangling-examples\\DATA\\boxscores

Run sqlite3 specifying the Boxscores.db database

In the sqlite3 REPL run the boxscores.sql script

**Contact/Links**

**You can contact me at:** [skeyes42@gmail.com](mailto:skeyes42@gmail.com) **and on LinkedIn.**
