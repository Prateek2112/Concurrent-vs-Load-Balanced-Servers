import pandas as pd

df = pd.read_csv("latency.csv", header = None)

avg = df.mean()

print("The average is:", avg)
