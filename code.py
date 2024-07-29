import pandas as pd

#reading the csv file
orders = pd.read_csv('orders.csv')
orders['order_date'] = pd.to_datetime(orders['order_date'])

orders['month'] = orders['order_date'].dt.to_period('M')
orders['revenue'] = orders['product_price'] * orders['quantity']

#Revenue for each month
monthly_revenue = orders.groupby('month')['revenue'].sum().reset_index()
monthly_revenue.columns = ['month', 'total_revenue']

#Revenue for each product
product_revenue = orders.groupby('product_id')['revenue'].sum().reset_index()
product_revenue.columns = ['product_id', 'total_revenue']

#Total revenue for each customer
customer_revenue = orders.groupby('customer_id')['revenue'].sum().reset_index()
customer_revenue.columns = ['customer_id', 'total_revenue']

#Top 10 customers
top_customers = customer_revenue.sort_values(by='total_revenue', ascending=False).head(10)

print("Total monthly revenue:")
print(monthly_revenue)

print("\nTotal product revenue")
print(product_revenue)

print("\nTotal Customer revenue:")
print(customer_revenue)

print("\nTop 10 customers:")
print(top_customers)
