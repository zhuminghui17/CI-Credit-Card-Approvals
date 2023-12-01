import pandas as pd

def read_data(path):
    """
    Read data from a given file path.
    """
    return pd.read_csv(path)

def describe_data(df):
    """
    Return a description of the data in the DataFrame.
    """
    return df.describe()

def head_data(df):
    """
    Return the first few rows of the DataFrame.
    """
    return df.head()

def missing_data(df):
    """
    Return the count of missing values in each column of the DataFrame.
    """
    return df.isnull().sum()

def null_data(df):
    """
    Return the count of null values in each column of the DataFrame.
    """
    return df.isna().sum()

def histogram(df):
    """
    Generate a histogram for the DataFrame.
    """
    return df.hist()

def correlation_matrix(df):
    """
    Return the correlation matrix of the DataFrame.
    """
    return df.corr()