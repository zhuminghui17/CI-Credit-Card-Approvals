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


# info
def info_data(df):
    """
    Info data
    Parameters
    ----------
    df : pd.DataFrame
        Dataframe containing data
    Returns
    -------
    info : pd.DataFrame
        Dataframe containing info
    """
    return df.info()


def head_data(df):
    """
    Head data
    Parameters
    ----------
    df : pd.DataFrame
        Dataframe containing data
        Returns
    ----------
    head : pd.DataFrame
        Dataframe containing head
    """
    return df.head()

def missing_data(df):
    """
    Missing data
    Parameters
    ----------
    df : pd.DataFrame
        Dataframe containing data
    Returns
    -------
    missing : pd.DataFrame
        Dataframe containing missing
    """
    return df.isnull().sum()

def null_data(df):
    """
    Null data
    Parameters
    ----------
    df : pd.DataFrame
        Dataframe containing data
    Returns
    -------
    null : pd.DataFrame
        Dataframe containing null
    """
    return df.isna().sum()

def histogram(df):
    """
    Histogram
    Parameters
    ----------
    df : pd.DataFrame
        Dataframe containing data
    Returns
    -------
    hist : pd.DataFrame
        Dataframe containing histogram
    """
    return df.hist()

def correlation_matrix(df):
    """
    Correlation matrix
    Parameters
    ----------
    df : pd.DataFrame
        Dataframe containing data
    Returns
    -------
    corr : pd.DataFrame
        Dataframe containing correlation matrix
    """
    return df.corr()