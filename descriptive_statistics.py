import lib

# read data
df = lib.read_data("credit_card_approvals.csv")

# EDA
pandas_stats = lib.describe_data(df)
print("Descriptive statistics using Pandas:")
print(pandas_stats)

head = lib.head_data(df)
print(head)
