import unittest
import pandas as pd
import lib


class TestDescriptiveStatistics(unittest.TestCase):
    def test_read_data(self):
        # Test read_data function
        df = lib.read_data("credit_card_approvals.csv")
        self.assertIsNotNone(df)
        self.assertIsInstance(df, pd.DataFrame)

    def test_describe(self):
        # Test describe_data function
        df = pd.DataFrame({"A": [1, 2, 3, 4, 5], "B": [5, 4, 3, 2, 1]})
        result = lib.describe_data(df)
        self.assertIsNotNone(result)
        self.assertIsInstance(result, pd.DataFrame)

    def test_head(self):
        # Test head_data function
        df = pd.DataFrame({"A": [1, 2, 3, 4, 5], "B": [5, 4, 3, 2, 1]})
        result = lib.head_data(df)
        self.assertIsNotNone(result)
        self.assertIsInstance(result, pd.DataFrame)

    def test_missing(self):
        # Test missing_data function
        df = pd.DataFrame({"A": [1, None, 3, 4, 5], "B": [5, 4, None, 2, 1]})
        result = lib.missing_data(df)
        self.assertIsNotNone(result)
        self.assertIsInstance(result, pd.Series)  # missing_data returns a Series

    def test_null(self):
        # Test null_data function
        df = pd.DataFrame({"A": [1, None, 3, 4, 5], "B": [5, 4, None, 2, 1]})
        result = lib.null_data(df)
        self.assertIsNotNone(result)
        self.assertIsInstance(result, pd.Series)  # null_data returns a Series

    def test_correlation(self):
        # Test correlation_matrix function
        df = pd.DataFrame({"A": [1, 2, 3, 4, 5], "B": [5, 4, 3, 2, 1]})
        result = lib.correlation_matrix(df)
        self.assertIsNotNone(result)
        self.assertIsInstance(result, pd.DataFrame)


if __name__ == "__main__":
    unittest.main()
