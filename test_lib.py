import unittest
import pandas as pd
import lib


class TestLibFunctions(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # This method is run once before all tests
        # Setup a DataFrame for testing
        cls.test_df = pd.DataFrame({"A": [10, 20, 30, 40, 50], "B": [5, 4, 3, 2, 1]})

    def test_read_data(self):
        df = lib.read_data("credit_card_approvals.csv")
        self.assertIsNotNone(df)
        self.assertIsInstance(df, pd.DataFrame)

    def test_describe_data(self):
        result = lib.describe_data(self.test_df)
        self.assertIsNotNone(result)
        self.assertIsInstance(result, pd.DataFrame)

    def test_head_data(self):
        result = lib.head_data(self.test_df)
        self.assertIsNotNone(result)
        self.assertIsInstance(result, pd.DataFrame)

    def test_missing_data(self):
        result = lib.missing_data(self.test_df)
        self.assertIsNotNone(result)
        self.assertIsInstance(result, pd.Series)

    def test_null_data(self):
        result = lib.null_data(self.test_df)
        self.assertIsNotNone(result)
        self.assertIsInstance(result, pd.Series)

    def test_correlation_matrix(self):
        result = lib.correlation_matrix(self.test_df)
        self.assertIsNotNone(result)
        self.assertIsInstance(result, pd.DataFrame)


if __name__ == "__main__":
    unittest.main()
