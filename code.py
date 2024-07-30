import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the CSV file
orders_df = pd.read_csv('/content/orders.csv')

# Compute total revenue for each order
orders_df['total_revenue'] = orders_df['product_price'] * orders_df['quantity']

# Converting order_date to datetime for month calculation and then calculating the monthly revenue
orders_df['order_date'] = pd.to_datetime(orders_df['order_date'])
orders_df['month'] = orders_df['order_date'].dt.to_period('M')
monthly_revenue = orders_df.groupby('month')['total_revenue'].sum().reset_index()
print("Monthly Revenue:")
print(monthly_revenue)

# Total revenue for each product
product_revenue = orders_df.groupby(['product_id', 'product_name'])['total_revenue'].sum().reset_index()
print("\nProduct Revenue:")
print(product_revenue)

# Total revenue for each customer
customer_revenue = orders_df.groupby('customer_id')['total_revenue'].sum().reset_index()
print("\nCustomer Revenue:")
print(customer_revenue)

# Top 10 customers
top_customers = customer_revenue.sort_values(by='total_revenue', ascending=False).head(10)
print("\nTop 10 Customers by Revenue:")
print(top_customers)
