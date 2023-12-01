import unittest
import pandas as pd
import lib


class TestDescriptiveStatistics(unittest.TestCase):
    def test_read_data(self):
        df = lib.read_data("credit_card_approvals.csv")
        self.assertIsNotNone(df)
        self.assertIsInstance(df, pd.DataFrame)

    def test_describe(self):
        df = pd.DataFrame({"A": [1, 2, 3, 4, 5], "B": [5, 4, 3, 2, 1]})
        result = lib.describe_data(df)
        self.assertIsNotNone(result)
        self.assertIsInstance(result, pd.DataFrame)


# Run the tests
if __name__ == "__main__":
    unittest.main()
