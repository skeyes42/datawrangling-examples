import pyRserve

def main():
    # Connect to Rserve (default host/port)
    conn = pyRserve.connect()

    # Evaluate a simple R expression
    result = conn.eval("mean(c(1, 2, 3, 4, 5))")
    print("Mean from R:", result)

    # Assign a Python list to an R variable
    conn.r.mydata = [10, 20, 30]

    # Use that variable inside R (convert list → numeric vector)
    sum_result = conn.eval("sum(as.numeric(mydata))")
    print("Sum from R:", sum_result)

    conn.close()

if __name__ == "__main__":
    main()