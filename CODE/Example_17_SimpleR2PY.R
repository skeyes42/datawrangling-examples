# Copyright 2025 by Steven J. Keyes. All rights reserved.
# FILE: Example_17a_SimpleR2PY.R
# DATE 2025-10-17
# DESCRIPTION: 

# This R function takes a numeric vector, performs a calculation,
# and returns a numeric vector.
process_data <- function(input_vector) {
  # Calculate the square root of each element
  results <- sqrt(input_vector)
  # Return the vector of results
  return(results)
}
