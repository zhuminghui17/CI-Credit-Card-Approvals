# Import the lib module
import lib

# Read data from the file 'credit_card_approvals.csv'
df = lib.read_data("credit_card_approvals.csv")

# Perform initial EDA using the functions from the lib module

# Get descriptive statistics using Pandas
pandas_stats = lib.describe_data(df)
print("Descriptive statistics using Pandas:")
print(pandas_stats)

# View the first few rows of the DataFrame
head = lib.head_data(df)
print("First few rows of the DataFrame:")
print(head)

# Check for missing data in each column
missing = lib.missing_data(df)
print("Missing data counts in each column:")
print(missing)

# Check for null data in each column
nulls = lib.null_data(df)
print("Null data counts in each column:")
print(nulls)

# Compute and display the correlation matrix
correlation = lib.correlation_matrix(df)
print("Correlation matrix of the DataFrame:")
print(correlation)
