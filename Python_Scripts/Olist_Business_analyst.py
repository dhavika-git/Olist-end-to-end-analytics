import pandas as pd
import numpy as np

geolocation = pd.read_csv('/Users/utsavsharma/Downloads/archive/geolocation_fixed.csv')
customer = pd.read_csv('/Users/utsavsharma/Downloads/archive/olist_customers_dataset.csv')
order_items_dataset = pd.read_csv('/Users/utsavsharma/Downloads/archive/olist_order_items_dataset.csv')
order_payments = pd.read_csv('/Users/utsavsharma/Downloads/archive/olist_order_payments_dataset.csv')
order_review = pd.read_csv('/Users/utsavsharma/Downloads/archive/olist_order_reviews_dataset.csv')
orders = pd.read_csv('/Users/utsavsharma/Downloads/archive/olist_orders_dataset.csv')
products = pd.read_csv('/Users/utsavsharma/Downloads/archive/olist_products_dataset.csv')
sellers = pd.read_csv('/Users/utsavsharma/Downloads/archive/olist_sellers_dataset.csv')
category_name_translation = pd.read_csv('/Users/utsavsharma/Downloads/archive/product_category_name_translation.csv')

''' 1. How many unique customers, orders, sellers, and products are in the dataset? '''
# print(customer['customer_id'].unique().size)
# print(orders['order_id'].unique().size)
# print(sellers['seller_id'].unique().size)
# print(products['product_id'].unique().size)

''' 2. What are the different order statuses, and what's the distribution (% of each)? '''
# print((orders['order_status'].value_counts(normalize=True) * 100).round(2))

# order_count = orders.groupby('order_status').size()
# percentage = (order_count / order_count.sum()) * 100
# print(percentage.round(2))

''' 3. Which product categories are available, and how many are there? '''
# print(products['product_category_name'].unique())
# print(products['product_category_name'].nunique())

''' 4. What is the total revenue generated? '''
# print('Revenue',order_payments['payment_value'].sum() )

''' 5. What is the average order value? '''
# avg = order_payments.groupby('order_id')['payment_value'].sum() 
# print('Average Order Value: ',avg.mean())

''' 6. Which months generated the highest revenue?'''
# df = orders.merge(order_payments, on = 'order_id')
# df['order_purchase_timestamp'] = pd.to_datetime(df['order_purchase_timestamp'] )

# df['Month'] = df['order_purchase_timestamp'].dt.month_name()  # month vise

# df['Year_month'] = df['order_purchase_timestamp'].dt.to_period('M')

# revenue1 = df.groupby('Month')['payment_value'].sum()
# print(revenue1)
# revenue2 =df.groupby('Year_month')['payment_value'].sum()
# print(revenue2)

''' 7. Is the marketplace growing over time? (plot revenue trend)'''
# df = orders.merge(order_payments, on = 'order_id')
# df['order_purchase_timestamp'] = pd.to_datetime(df['order_purchase_timestamp'] )
# df['Year_month'] = df['order_purchase_timestamp'].dt.to_period('M')
# revenue = df.groupby('Year_month')['payment_value'].sum()
# print(revenue.sort_values(ascending = True))

# ''' 8. Which year had the highest sales?'''
# df = orders.merge(order_payments, on = 'order_id')
# df['order_purchase_timestamp'] = pd.to_datetime(df['order_purchase_timestamp'])
# df['year'] = df['order_purchase_timestamp'].dt.year
# rev = df.groupby('year')['payment_value'].sum()
# print(rev.sort_values(ascending=False))

''' 9. What percentage growth did revenue experience year-over-year?'''
# df = orders.merge(order_payments, on = 'order_id')
# df['order_purchase_timestamp'] = pd.to_datetime(df['order_purchase_timestamp'])
# df['year'] = df['order_purchase_timestamp'].dt.year
# rev = df.groupby('year')['payment_value'].sum()
# print((rev.pct_change()*100).round(2))

''' 10. Which states have the highest number of customers? '''
# print(customer.groupby('customer_state')['customer_id'].size().sort_values(ascending=False).idxmax())
# print(customer['customer_state'].value_counts().idxmax())

''' 11. Which cities contribute the most customers? '''
# print(customer.groupby('customer_city')['customer_id'].size().sort_values(ascending=False).idxmax())
# print(customer['customer_city'].value_counts().idxmax())

''' 12. What is the average spending per customer? '''
# df = customer.merge(orders, on = 'customer_id').merge(order_payments, on = 'order_id')
# spending = df.groupby('customer_id')['payment_value'].sum()
# print(spending.mean())

''' 13. Who are the top 20 customers by total spending? '''
# df = customer.merge(orders, on = 'customer_id').merge(order_payments, on = 'order_id')
# spending = df.groupby('customer_id')['payment_value'].sum()
# print(spending.head(20).sort_values(ascending=False))

''' 14. What percentage of customers made repeat purchases? '''
# order = orders.groupby('customer_id')['order_id'].count()
# repeat_cus =  order.gt(1).sum()
# total_order = order.count()
# percentage = (repeat_cus / total_order) * 100
# print(percentage)

''' 15. Which customers can be classified as VIP based on spending (e.g., top 5%)? '''
# df = customer.merge(orders, on = 'customer_id').merge(order_payments, on = 'order_id')
# spending = df.groupby('customer_id')['payment_value'].sum()
# VIP_criteria = spending.quantile(0.95)
# VIP = spending[spending >= VIP_criteria]
# print(VIP)

''' 16. Which product categories generate the highest revenue?'''
# df = order_payments.merge(order_items_dataset, on = 'order_id').merge(products, on = 'product_id')
# print(df.groupby('product_category_name')['price'].sum().sort_values(ascending=False).head(1))

''' 17. Which categories sell the highest number of units?'''
# df = order_items_dataset.merge(products, on = 'product_id')
# print(df.groupby('product_category_name')['order_item_id'].count().sort_values(ascending=False).head(1))

''' 18. Which product categories are the least popular?'''
# df = order_items_dataset.merge(products, on = 'product_id')
# print(df.groupby('product_category_name')['order_item_id'].count().sort_values(ascending=False).tail(1))

''' 19.Which individual products contribute the most revenue?'''
# df = order_items_dataset.merge(products, on='product_id')
# print(df.groupby('product_id')['price'].sum().sort_values(ascending=False).head(1))

''' 20. Which categories have high sales but low customer ratings? (this needs a merge with reviews — good multi-table practice)'''
# df = order_items_dataset.merge(products, on = 'product_id')
# category_highest_sale = (df.groupby('product_category_name')['price'].sum().sort_values(ascending=False).reset_index())

# df2 = order_review.merge(order_items_dataset, on = 'order_id').merge(products, on = 'product_id')
# min_review = (df2.groupby('product_category_name')['review_score'].mean().sort_values().reset_index())

# highest_sale_and_lowest_review = category_highest_sale.merge(min_review, on = 'product_category_name').sort_values(by=['price', 'review_score'], ascending=[False, True])
# print(highest_sale_and_lowest_review)

''' 21. Which sellers generate the highest revenue?'''
# df = order_items_dataset.merge(sellers, on='seller_id')
# highest_revenue = (df.groupby('seller_id')['price'].sum().sort_values(ascending=False))
# print(highest_revenue.head(1))

''' 22. Which sellers process the highest number of orders?'''
# df = order_items_dataset.merge(sellers, on='seller_id')
# highest_orders = (df.groupby('seller_id')['order_id'].nunique().sort_values(ascending=False))
# print(highest_orders.head(1))

''' 23. Which sellers have the best average customer ratings?'''
# df = order_review.merge(order_items_dataset, on='order_id')
# best_sellers = (df.groupby('seller_id')['review_score'].mean().sort_values(ascending=False))
# print(best_sellers.head(1))

''' 24. Which sellers have consistently poor ratings?'''
# df = order_review.merge(order_items_dataset, on='order_id')
# poor_sellers = (df.groupby('seller_id')['review_score'].mean().sort_values().reset_index())
# print(poor_sellers.head(10))

''' 25. What is the average delivery time (purchase to delivery)?'''
# orders['order_delivered_customer_date'] = pd.to_datetime(orders['order_delivered_customer_date'])
# orders['order_purchase_timestamp'] = pd.to_datetime(orders['order_purchase_timestamp'])

# orders['difference'] = orders['order_delivered_customer_date'] - orders['order_purchase_timestamp'] 
# print(orders['difference'].dt.days.mean() )

''' 26. Which states experience the longest delivery times?'''
# df = orders.merge(customer, on = 'customer_id')
# df['order_delivered_customer_date'] = pd.to_datetime(df['order_delivered_customer_date'])
# df['order_purchase_timestamp'] = pd.to_datetime(df['order_purchase_timestamp'])

# df['difference'] = (df['order_delivered_customer_date'] - df['order_purchase_timestamp']).dt.days 
# print(df.groupby('customer_state')['difference'].mean().sort_values(ascending=False))

''' 27. Which sellers have the fastest delivery performance?'''
# df = orders.merge(order_items_dataset, on = 'order_id').merge(sellers, on = 'seller_id')
# df['order_delivered_customer_date'] = pd.to_datetime(df['order_delivered_customer_date'])
# df['order_purchase_timestamp'] = pd.to_datetime(df['order_purchase_timestamp'])

# df['delivery_days'] = (df['order_delivered_customer_date']  - df['order_purchase_timestamp']).dt.days
# seller_delievery_performance = df.groupby('seller_id')['delivery_days'].mean().reset_index()

''' 28. Does longer delivery time negatively impact customer reviews? (correlation/groupby comparison)'''
# df = orders.merge(order_review, on='order_id').merge(order_items_dataset, on='order_id').merge(sellers, on='seller_id')
# df['order_delivered_customer_date'] = pd.to_datetime(df['order_delivered_customer_date'])
# df['order_purchase_timestamp'] = pd.to_datetime(df['order_purchase_timestamp'])

# df['delivery_days'] = (df['order_delivered_customer_date'] > df['order_purchase_timestamp'])
# seller_delievery_performance = df.groupby('seller_id')['delivery_days'].mean().reset_index()
# result = df.groupby('delivery_days')['review_score'].mean().reset_index()

# print(df[['delivery_days', 'review_score']].corr())

''' 29. Are delayed orders (delivered after estimated date) associated with lower review scores?'''

# df = orders.merge(order_review, on='order_id').merge(order_items_dataset, on='order_id').merge(sellers, on='seller_id')
# df['order_delivered_customer_date'] = pd.to_datetime(df['order_delivered_customer_date'])
# df['order_purchase_timestamp'] = pd.to_datetime(df['order_purchase_timestamp'])

# df['delivery_days'] = (df['order_delivered_customer_date'] > df['order_purchase_timestamp'])
# seller_delievery_performance = df.groupby('seller_id')['delivery_days'].mean().reset_index()

# result = df.groupby('delivery_days')['review_score'].mean().reset_index()
# print(result)

''' 30. Which payment methods are most frequently used?'''
# print(order_payments.groupby('payment_type')['payment_type'].count())

''' 31. Which payment methods contribute the highest revenue?'''
# print(order_payments.groupby('payment_type')['payment_value'].sum().sort_values(ascending=False))

''' 32. What is the average installment count for each payment type?'''
# print(order_payments.groupby('payment_type')['payment_installments'].mean().sort_values(ascending=False))

''' 33. Do customers using installments spend more on average than single-payment customers?'''
# installment_spend = order_payments[order_payments['payment_installments'] > 1]['payment_value'].mean()
# single_installment = order_payments[order_payments['payment_installments'] == 1]['payment_value'].mean()

# if installment_spend > single_installment:
#     print(True)
# else:
#     print(False)

''' 34. What is the distribution of review scores (1-5)?'''
# print(order_review.groupby('review_score')['order_id'].count())

''' 35. Which product categories receive the highest and lowest average ratings?'''
# df = order_review.merge(order_items_dataset, on = 'order_id').merge(products, on ='product_id')
# product_vise_review = df.groupby('product_category_name')['review_score'].mean()
# print(product_vise_review.idxmax(), '=' , product_vise_review.max())
# print(product_vise_review.idxmin(), '=' , product_vise_review.min())

''' 36. How do review scores vary by seller?'''
# df = order_review.merge(order_items_dataset, on='order_id')
# seller_reviews = df.groupby('seller_id')['review_score'].mean().sort_values(ascending=False)
# print(seller_reviews)

''' 37. How do monthly order volumes fluctuate across the dataset?'''
# orders['order_purchase_timestamp'] = pd.to_datetime(orders['order_purchase_timestamp'])
# orders['year_month'] = orders['order_purchase_timestamp'].dt.to_period('M')
# print(orders.groupby('year_month')['order_id'].count())


''' 38. Which months are consistently the busiest?'''
# orders['order_purchase_timestamp'] = pd.to_datetime(orders['order_purchase_timestamp'])
# orders['month'] = orders['order_purchase_timestamp'].dt.month_name()
# print(orders.groupby('month')['order_id'].count().sort_values(ascending=False))

''' 39. Based on your findings, which 3-5 product categories should Olist prioritize for growth?'''

# ''' 1st approach : By Revenue '''
# df = order_items_dataset.merge(products, on='product_id').merge(category_name_translation, on='product_category_name')
# top_revenue = (df.groupby('product_category_name_english')['price'].sum().sort_values(ascending=False).head(10))
# print(top_revenue)

# ''' 1st approach : By review '''
# df = order_items_dataset.merge(products, on='product_id').merge(category_name_translation, on='product_category_name').merge(order_review, on='order_id')
# top_reviews = (df.groupby('product_category_name_english')['review_score'].mean().sort_values(ascending=False).head(10))
# print(top_reviews)

''' 40. Which regions need logistics improvements, and why (back it with your delivery-delay numbers)?'''
''' 41. What are your top 5 actionable business recommendations?'''

''' 1. Customers Dataset (olist_customers_dataset.csv)
Check
Duplicate rows
Duplicate customer_id
Missing values
Data types      '''

# print(customer.info())
# print(customer.duplicated().sum())
# print(customer['customer_id'].duplicated().sum())
# print(customer.isnull().sum())
# print(customer.dtypes)


# customer.to_csv('customer_cleaned_dataset.csv',index=False)

''' 2. Orders Dataset (olist_orders_dataset.csv)
Check : 
Missing values
Duplicate order_id
Date formats
Invalid delivery dates  '''


# (orders.duplicated().sum())
# (orders['order_id'].duplicated().sum())
# print(orders.isnull().sum())
# # (orders.fillna('Empty',inplace=True))

# (orders.to_csv("olist_orders_dataset_cleaned.csv", index=False))
# (orders.info())


# orders.to_csv("olist_orders_dataset_cleaned.csv", index=False)

'''
3. Order Items Dataset
Check :
Duplicate rows
Missing values
Negative prices
Negative freight values. '''
# print(order_items_dataset.duplicated().sum())
# print(order_items_dataset.isnull().sum())
# print((order_items_dataset['freight_value']< 0).sum())
# print((order_items_dataset['price']< 0).sum())

# order_items_dataset.to_csv('order_items_dataset_cleaned.csv',index=False)

'''
4. Order Payments Dataset
Check :
Missing values
Negative payment value
Negative installments'''

# print(order_payments.isnull().sum())
# print((order_payments['payment_value'] < 0).sum())
# print((order_payments['payment_installments'] < 0).sum())

# order_payments.to_csv("olist_order_payments_dataset_cleaned.csv", index=False)

'''
5. Reviews Dataset
Check :
Missing values
Review score '''
# print(order_review['review_score'].isnull().sum())
# print(order_review['review_score'].value_counts().sort_index())
# print(((order_review['review_score'] < 1) | (order_review['review_score'] > 5)).sum())

# order_review.to_csv('order_review_cleaned.csv',index=False)

'''
6. Products Dataset
Check :
Missing values
Duplicate product_id
Product dimensions
Weight. '''

# products['product_category_name'].fillna('Unknown', inplace=True)
''' Fill emply product category name '''
# products['product_category_name'] = products['product_category_name'].fillna('Unknown')
# print(products.isnull().sum())

# print(products['product_id'].duplicated().sum())
# print((products['product_length_cm'] <= 0).sum())
# print((products['product_height_cm'] <= 0).sum())
# print((products['product_width_cm'] <= 0).sum())
# print((products['product_weight_g'] <= 0).sum())

''' Since product_weight_g is having 4 raws which is having = 0, so will remove these '''
# products.drop(products[products['product_weight_g'] <= 0].index, inplace=True)

# products.to_csv("products_cleaned_dataset.csv", index=False)

'''
7. Sellers Dataset
Check :
Duplicate check
Missing values '''
# print(sellers.duplicated().sum())
# print(sellers.isnull().sum())

# sellers.to_csv('seller_cleared.csv',index=False)

'''
8. Category Translation Dataset
Check : 
Duplicate category names.'''
# print(category_name_translation.duplicated().sum())
# category_name_translation.to_csv('category_name_translation_cleared.csv',index=False)

# completed