import pandas as pd
products=['Apples', 'Bananas', 'Oranges', 'Grapes', 'Pineapples','Mangoes', 'Pears']
sales=[150, 200, 250, 300, 350, 400, 450]
sales_series = pd.Series(sales, index=products)
print(sales_series['Apples'])
print(sales_series['Bananas'])
total_sales = sales_series.sum()
print(total_sales)
best_selling_product=sales_series.idxmax()
print(best_selling_product)