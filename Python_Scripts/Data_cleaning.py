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

''' ------------------------------------------------------------------------------------------'''

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

#