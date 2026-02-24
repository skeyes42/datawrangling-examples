import pyRserve
import pandas as pd

def main():
    # Sample pandas DataFrame
    df = pd.DataFrame({
        "x": [1, 2, 3, 4],
        "y": [10, 20, 30, 40]
    })

    # Connect to Rserve
    conn = pyRserve.connect()

    # Send each column separately (pyRserve can serialize lists)
    conn.r.x = df["x"].tolist()
    conn.r.y = df["y"].tolist()

    # Build the data.frame inside R
    conn.eval("mydata <- data.frame(x = as.numeric(x), y = as.numeric(y))")

    # Use it in R
    mean_y = conn.eval("mean(mydata$y)")
    print("Mean of y from R:", mean_y)

    summary = conn.eval("summary(mydata)")
    print("R summary(mydata):")
    print(summary)

    conn.close()

if __name__ == "__main__":
    main()