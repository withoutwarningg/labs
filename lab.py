import json

def calculate_product_sum(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
        product_sum = sum(item['score'] * item['weight'] for item in data)
        rounded_sum = round(product_sum, 3)
        print(rounded_sum)
        return rounded_sum


calculate_product_sum('data.json')