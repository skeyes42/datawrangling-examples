# Copyright 2025 by Steven J. Keyes. All rights reserved.
# FILE: DisplayDataframeWeb.R
# DATE 2025-10-25
# DESCRIPTION: 
# This program is a web application built with R Shiny, a framework used 
# to create interactive data dashboards. It allows users to view, search, 
# and filter the "Boxscores" database through a professional web interface.

library(shiny)
library(DT)
library(RSQLite)
library(DBI)
library(dplyr)

# Connect to database
path_to_database <- file.path(Sys.getenv("EXAMPLES"), "Boxscores.db")
con <- dbConnect(RSQLite::SQLite(), path_to_database)

query <- tbl(con, "Boxscores") |>
           select(everything())

results_df <- query |>
  collect()
  
dbDisconnect(con)

# UI
ui <- fluidPage(
  titlePanel("Dataframe Display"),
  
  sidebarLayout(
    sidebarPanel(
      h4("Data Information"),
      textOutput("info"),
      hr(),
      p("Use the search box and column filters to explore the data.")
    ),
    
    mainPanel(
      DTOutput("table")
    )
  )
)

# Server
server <- function(input, output, session) {
  
  output$info <- renderText({
    paste("Rows:", nrow(results_df), "| Columns:", ncol(results_df))
  })
  
  output$table <- renderDT({
    datatable(
      results_df,
      options = list(
        pageLength = 10,
        searching = TRUE,
        ordering = TRUE
      ),
      filter = "top",
      rownames = FALSE
    )
  })
}

# Run the app
shinyApp(ui = ui, server = server)

################################################################################################
# To run: In editor: (1) Highlight line 59 (2) Hit Ctrl-Enter                                  #
################################################################################################
