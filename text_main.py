import unittest
import pandas as pd
from io import StringIO

class RevenueTestCases(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Sample data in CSV format
        data = """order_id,customer_id,order_date,product_id,product_name,product_price,quantity
1,1,2023-01-01,101,Item X,120,2
2,2,2023-01-05,102,Item Y,250,1
3,1,2023-02-10,101,Item X,120,4
4,3,2023-02-15,103,Item Z,350,1
5,4,2023-03-20,104,Item W,450,3
"""
        # Load the CSV data into a DataFrame
        cls.df = pd.read_csv(StringIO(data))
        cls.df['order_date'] = pd.to_datetime(cls.df['order_date'])
        cls.df['revenue'] = cls.df['product_price'] * cls.df['quantity']
        cls.df['period'] = cls.df['order_date'].dt.to_period('M')

    def test_revenue_by_month(self):
        monthly_totals = self.df.groupby('period')['revenue'].sum().reset_index()
        expected_monthly_revenue = {
            'period': ['2023-01', '2023-02', '2023-03'],
            'revenue': [240, 560, 1350]
        }
        expected_df = pd.DataFrame(expected_monthly_revenue)
        pd.testing.assert_frame_equal(monthly_totals, expected_df)

    def test_revenue_by_product(self):
        product_totals = self.df.groupby(['product_id', 'product_name'])['revenue'].sum().reset_index()
        expected_product_revenue = {
            'product_id': [101, 102, 103, 104],
            'product_name': ['Item X', 'Item Y', 'Item Z', 'Item W'],
            'revenue': [480, 250, 350, 1350]
        }
        expected_df = pd.DataFrame(expected_product_revenue)
        pd.testing.assert_frame_equal(product_totals, expected_df)

    def test_revenue_by_customer(self):
        customer_totals = self.df.groupby('customer_id')['revenue'].sum().reset_index()
        expected_customer_revenue = {
            'customer_id': [1, 2, 3, 4],
            'revenue': [600, 250, 350, 1350]
        }
        expected_df = pd.DataFrame(expected_customer_revenue)
        pd.testing.assert_frame_equal(customer_totals, expected_df)

    def test_top_customers_by_revenue(self):
        customer_totals = self.df.groupby('customer_id')['revenue'].sum().reset_index()
        top_customers = customer_totals.sort_values(by='revenue', ascending=False).head(10)
        expected_top_customers = {
            'customer_id': [4, 1, 3, 2],
            'revenue': [1350, 600, 350, 250]
        }
        expected_df = pd.DataFrame(expected_top_customers)
        pd.testing.assert_frame_equal(top_customers, expected_df)

if __name__ == '__main__':
    unittest.main()
