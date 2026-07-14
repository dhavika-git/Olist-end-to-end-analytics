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

'''-------------------------------------------------------------------'''

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

states = [customer['customer_state'].isin(['SP', 'RJ', 'MG', 'ES']), 
          customer['customer_state'].isin(['PR', 'RS', 'SC']),
          customer['customer_state'].isin(['GO', 'MT', 'MS', 'DF']),
          customer['customer_state'].isin(['BA', 'CE', 'RN', 'PE', 'PB', 'PI', 'AL', 'SE', 'MA']),
          customer['customer_state'].isin(['PA', 'AM', 'AP', 'RO', 'TO', 'AC', 'RR'])]

region = ['Southeast','South','Central-West','Northeast','North']
customer['customer_region'] = np.select(states, region, default='Unknown')

''' Add necessary columns '''

customer.to_csv('customer_cleaned_dataset.csv',index=False)

''' 2. Orders Dataset (olist_orders_dataset.csv)
Check : 
Missing values
Duplicate order_id
Date formats
Invalid delivery dates  '''

# orders['order_purchase_timestamp'] = pd.to_datetime(orders['order_purchase_timestamp'] )
# orders['order_approved_at'] = pd.to_datetime(orders['order_approved_at'])
# orders['order_delivered_carrier_date'] = pd.to_datetime(orders['order_delivered_carrier_date'])
# orders['order_delivered_customer_date'] = pd.to_datetime(orders['order_delivered_customer_date'])
# orders['order_estimated_delivery_date'] = pd.to_datetime(orders['order_estimated_delivery_date'])

# invalid_dates = orders[ orders['order_delivered_customer_date'] < orders['order_purchase_timestamp']]
# print(invalid_dates)

# (orders.duplicated().sum())
# (orders['order_id'].duplicated().sum())
# print(orders.isnull().sum())
# # (orders.fillna('Empty',inplace=True))

# (orders.info())

''' Add necessary columns '''
# converting the columns  into date_time

orders['order_delivered_customer_date'] = pd.to_datetime(orders['order_delivered_customer_date'])
orders['order_purchase_timestamp'] = pd.to_datetime(orders['order_purchase_timestamp'])
orders['order_approved_at'] = pd.to_datetime(orders['order_approved_at'])
orders['order_delivered_carrier_date'] = pd.to_datetime(orders['order_delivered_carrier_date'])
orders['order_estimated_delivery_date'] = pd.to_datetime(orders['order_estimated_delivery_date'])

orders['delivery_days'] = (orders['order_delivered_customer_date'] - orders['order_purchase_timestamp']).dt.days
orders['approval_days'] = (orders['order_approved_at'] -orders['order_purchase_timestamp']).dt.days
orders['carrier_pickup_days'] = (orders['order_delivered_carrier_date'] -orders['order_approved_at']).dt.days
orders['estimated_delivery_days'] = (orders['order_estimated_delivery_date'] -orders['order_purchase_timestamp']).dt.days
orders['delivery_delay_days'] = (orders['order_delivered_customer_date'] - orders['order_estimated_delivery_date']).dt.days
orders['is_delayed'] = (orders['order_delivered_customer_date'] > orders['order_estimated_delivery_date'])
orders['purchase_year'] = orders['order_purchase_timestamp'].dt.year
orders['purchase_month'] = orders['order_purchase_timestamp'].dt.month
orders['purchase_month_name'] = orders['order_purchase_timestamp'].dt.month_name()
orders['purchage_quarter'] = orders['order_purchase_timestamp'].dt.quarter
orders['purchage_day'] = orders['order_purchase_timestamp'].dt.day
orders['purchage_weekday'] = orders['order_purchase_timestamp'].dt.day_name()
orders['purchage_hour'] = orders['order_purchase_timestamp'].dt.hour
orders['is_weekend_order'] = orders['order_purchase_timestamp'].dt.day_name().isin(['Saturday','Sunday'])

# print(orders['delivery_days'])
# print(orders['approval_days'] )
# print(orders['carrier_pickup_days'])
# print(orders['estimated_delivery_days'])
# print(orders['delivery_delay_days'])

orders.to_csv("orders_cleaned_dataset.csv", index=False)

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

order_items_dataset['total_item_cost'] = (order_items_dataset['price'] + order_items_dataset['freight_value'])
order_items_dataset['freight_percentage'] = (order_items_dataset['freight_value'] / order_items_dataset['price']) * 100
order_items_dataset['is_free_shipping'] = order_items_dataset['freight_value'] < 1

order_items_dataset.to_csv('order_items_cleaned_dataset.csv',index=False)

'''
4. Order Payments Dataset
Check :
Missing values
Negative payment value
Negative installments'''

# print(order_payments.isnull().sum())
# print((order_payments['payment_value'] < 0).sum())
# print((order_payments['payment_installments'] < 0).sum())

order_payments['is_installment'] = (order_payments.groupby('order_id')['payment_installments'].transform('max') > 1)
# print(order_payments['is_installment'].value_counts() )

''' High-value payment flag '''

criteria = order_payments['payment_value'].quantile(0.90)
order_payments['high_value_payment'] = order_payments['payment_value'] >= criteria

order_payments.to_csv("order_payments_cleaned_dataset.csv", index=False)

'''
5. Reviews Dataset
Check :
Missing values
Review score '''
# print(order_review['review_score'].isnull().sum())
# print(order_review['review_score'].value_counts().sort_index())
# print(((order_review['review_score'] < 1) | (order_review['review_score'] > 5)).sum())

conditions = [order_review['review_score']<= 2, order_review['review_score'] >= 4]
choice = ['Negative', 'Positive']
order_review['review_category'] = np.select(conditions, choice, default= 'Neutral')

order_review.to_csv('order_review_cleaned_dataset.csv',index=False)

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

conditions = [products['product_weight_g'] <= 500,
             (products['product_weight_g'] > 500) & (products['product_weight_g'] <= 2000),
              products['product_weight_g'] > 2000  ]

choices = ['Light', 'Medium', 'Heavy']
products['weight_category'] = np.select( conditions, choices, default='Unknown')

products.to_csv("products_cleaned_dataset.csv", index=False)

'''
7. Sellers Dataset
Check :
Duplicate check
Missing values '''
# print(sellers.duplicated().sum())
# print(sellers.isnull().sum())

seller_states = [sellers['seller_state'].isin(['SP', 'RJ', 'MG', 'ES']), 
                sellers['seller_state'].isin(['PR', 'RS', 'SC']),
                sellers['seller_state'].isin(['GO', 'MT', 'MS', 'DF']),
                sellers['seller_state'].isin(['BA', 'CE', 'RN', 'PE', 'PB', 'PI', 'AL', 'SE', 'MA']),
                sellers['seller_state'].isin(['PA', 'AM', 'AP', 'RO', 'TO', 'AC', 'RR'])]

region = ['Southeast','South','Central-West','Northeast','North']
sellers['seller_state'] = np.select(seller_states, region, default='Unknown')

sellers.to_csv('seller_cleared.csv',index=False)

'''
8. Category Translation Dataset
Check : 
Duplicate category names.'''
# print(category_name_translation.duplicated().sum())

category_name_translation.to_csv('category_name_translation_cleared.csv',index=False)