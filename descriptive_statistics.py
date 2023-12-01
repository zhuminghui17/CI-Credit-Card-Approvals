import lib

# read data
df = lib.read_data("iris.csv")

# EDA
pandas_stats = lib.describe_data(df)
print("Descriptive statistics using Pandas:")
print(pandas_stats)
