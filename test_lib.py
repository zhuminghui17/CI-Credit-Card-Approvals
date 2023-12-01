
import unittest
import pandas as pd
from lib import generate_data, describe_with_pandas

class TestLibFunctions(unittest.TestCase):

    def test_generate_data_csv(self):
        df = generate_data("iris.csv")
        self.assertIsNotNone(df)
        self.assertIsInstance(df, pd.DataFrame)

    def test_describe_with_pandas(self):
        df = pd.DataFrame({
            'A': [1, 2, 3, 4, 5],
            'B': [5, 4, 3, 2, 1]
        })
        result = describe_with_pandas(df)
        self.assertIsNotNone(result)
        self.assertIsInstance(result, pd.DataFrame)

# Run the tests
if __name__ == '__main__':
    unittest.main()