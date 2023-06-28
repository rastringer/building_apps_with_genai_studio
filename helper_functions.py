# Helper functions from DeepLearning AI's excellent 'Building Systems with the ChatGPT API' course
# https://learn.deeplearning.ai/chatgpt-building-system

import json 
from collections import defaultdict

products_file = "products.json"

def get_products():
    with open(products_file, 'r') as file:
        products = json.load(file)
    return products

products = get_products()

def read_string_to_list(input_string):
    if input_string is None:
        return None

    try:
        input_string = input_string.replace("'", "\"")  # Replace single quotes with double quotes for valid JSON
        data = json.loads(input_string)
        return data
    except json.JSONDecodeError:
        print("Error: Invalid JSON string")
        return None   
    
def get_product_by_name(name):
    return products.get(name, None)

def get_products_by_category(category):
    products = get_products()
    return [product for product in products.values() if product["category"] == category]

def generate_output_string(data_list):
    output_string = ""

    if data_list is None:
        return output_string

    for data in data_list:
        try:
            if "products" in data:
                products_list = data["products"]
                for product_name in products_list:
                    product = get_product_by_name(product_name)
                    if product:
                        output_string += json.dumps(product, indent=4) + "\n"
                    else:
                        print(f"Error: Product '{product_name}' not found")
            elif "category" in data:
                category_name = data["category"]
                category_products = get_products_by_category(category_name)
                for product in category_products:
                    output_string += json.dumps(product, indent=4) + "\n"
            else:
                print("Error: Invalid object format")
        except Exception as e:
            print(f"Error: {e}")

    return output_string 

def generate_category_product_list(response):
    temp_str = str(response).strip()
    category_and_product_list = read_string_to_list(temp_str)
    return category_and_product_list
