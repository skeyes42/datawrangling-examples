# Ensure the S7 package is installed and loaded
# install.packages("S7")
library(S7)

# 1. Define the S7 Class
# We define a simple 'Person' class with a 'name' property of type character.
Person <- new_class(
  "Person",
  properties = list(
    name = class_character
  )
)

# 2. Create a new S7 Generic Function
# This generic will dispatch based on the 'x' argument.
greet <- new_generic(
  name = "greet",
  dispatch_args = "x"
)

# 3. Define Methods for the Generic

# Method for the 'Person' class
method(greet, Person) <- function(x, ...) {
  paste("Hello,", x@name, "!")
}

# Method for the base 'class_character' type
method(greet, class_character) <- function(x, ...) {
  paste("Hello, mysterious character vector:", x)
}

# 4. Usage Examples

# Create an object of the 'Person' class
john <- Person(name = "John Doe")

# Call the generic function with the 'Person' object (dispatches to the Person method)
print(
  greet(john)
)

# Call the generic function with a base R type (dispatches to the class_character method)
print(
  greet("Jane")
)
