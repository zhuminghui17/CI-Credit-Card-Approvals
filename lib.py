import pandas as pd

def read_data(path):
    """
    Read data from path
    Parameters
    ----------
    path : str
        Path to data
    Returns
    -------
    data : pd.DataFrame
        Dataframe containing data
    """
    return pd.read_csv(path)


def describe_data(df):
    """
    Describe data
    Parameters
    ----------
    df : pd.DataFrame
        Dataframe containing data
    """
    return df.describe()

