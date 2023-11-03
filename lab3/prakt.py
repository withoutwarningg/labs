def calculate_total_sales(sales_list):
    total_sales = 0

    for sale in sales_list:
        quantity = sale["quantity"]
        price_per_unit = sale["price_per_unit"]
        total_sales += quantity * price_per_unit

    return total_sales


sales = [
    {"product": "Товар 1", "quantity": 3, "price_per_unit": 10},
    {"product": "Товар 2", "quantity": 5, "price_per_unit": 15},
    {"product": "Товар 3", "quantity": 2, "price_per_unit": 20}
]

total = calculate_total_sales(sales)
print(total)