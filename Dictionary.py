Q. Suppose you are building a stock tracking application that allows users to track the prices of different stocks. You decide to use a dictionary to store the stock information, where each stock symbol is the key and the
corresponding value is a dictionary that contains the stock name, price, and other details.
Your application should allow users to add new stocks to track, remove existing stocks, and update the prices of stocks.
Write a function in Python that takes in a stock symbol and a new price and updates the price for that stock in the dictionary. The function should also print a message confirming the update.

stock_info = {}

def add():
    stock_symbol = input("Enter the stock symbol: ")
    stock_name = input("Enter the stock name: ")
    stock_price = float(input("Enter the stock price: "))
    stock_info[stock_symbol] = {'name': stock_name, 'price': stock_price}
    print("Stock ",stock_symbol ,"-" ,stock_name ,"has been added with a price of",stock_price ,"Rs.")

def remove():
    stock_symbol = input("Enter the stock symbol to remove: ")
    if stock_symbol in stock_info:
        del stock_info[stock_symbol]
        print("Stock",stock_symbol," has been removed from the tracking list.")
    else:
        print("Stock with symbol ",stock_symbol  ,"not found in the tracking list.")

def update():
    stock_symbol = input("Enter the stock symbol: ")
    new_stock_price = float(input("Enter the new stock price: "))

    if stock_symbol in stock_info:
        stock_info[stock_symbol]['price'] = new_stock_price
        print("Price for ",stock_symbol ,"has been updated to",new_stock_price,"Rs.")
    else:
        print("Stock with symbol ",stock_symbol, "not found. Please add it first.")
def show():
    if stock_info:
        print("All stocks:")
        for stock_symbol, data in stock_info.items():
            print("Symbol: ",stock_symbol, "Name: ",data['name'], "Price:", data['price'],"Rs")
    else:
        print("There is no stock")

while True:
    print("Choose an option:")
    print("1. Add a new stock")
    print("2. Remove a stock")
    print("3. Update stock price")
    print("4. Show the all stock")
    print("5. Exit")

    option = input("Enter your choice: ")

    if option == '1':
       add()
    elif option == '2':
      remove()
    elif option == '3':
      update()
    elif option == '4':
       show()
    elif option == '5':
        break
    else:
        print("Invalid option. Please select a valid option.")


Q. Suppose you are working on a project that requires you to store information about various products in a dictionary. Each product is identified by
a unique product ID, and the corresponding value in the dictionary is a dictionary that contains details about the product, such as its name,
description, price, and stock level.
You need to write a function in Python that takes in the dictionary of products and returns the product ID of the product with the lowest price. 
If there are multiple products with the same lowest price, the function should return the product ID of the first such product encountered.

products = {}

def add_product():
    product_id = input("Enter the product ID: ")
    name = input("Enter the product name: ")
    description = input("Enter the product description: ")
    price = float(input("Enter the product price: "))
    stock = int(input("Enter the product stock level: "))

    if product_id not in products:
        products[product_id] = {
            "name": name,
            "description": description,
            "price": price,
            "stock": stock
        }
        print(f"Product {product_id} has been added to the database.")
    else:
        print(f"Product {product_id} already exists in the database.")

def remove_product(product_id):
    if product_id in products:
        del products[product_id]
        print(f"Product {product_id} has been removed from the database.")
    else:
        print(f"Product {product_id} not found in the database.")

def update_product(product_id, field, new_value):
    if product_id in products:
        if field in products[product_id]:
            products[product_id][field] = new_value
            print(f"{field} for Product {product_id} has been updated to {new_value}.")
        else:
            print(f"{field} is not a valid field for Product {product_id}.")
    else:
        print(f"Product {product_id} not found in the database.")

def display_products():
    if not products:
        print("No products found in the database.")
    else:
        print("Product ID  Name           Description     Price  Stock")
        for product_id, product_info in products.items():
            print(f"{product_id:<12} {product_info['name']:<15} {product_info['description']:<15} {product_info['price']:<7} {product_info['stock']}")

def find_product_with_lowest_price(product_dict):
    if not product_dict:
        return None

    lowest_price = float()
    lowest_price_product_id = None

    for product_id, product_info in product_dict.items():
        if "price" in product_info:
            price = product_info["price"]
            if price < lowest_price:
                lowest_price = price
                lowest_price_product_id = product_id

    return lowest_price_product_id

while True:
    print("Choose an option:")
    print("1. Add a new product")
    print("2. Remove a product")
    print("3. Update product information")
    print("4. Display all products")
    print("5. Find product with the lowest price")
    print("6. Exit")

    option = input("Enter your choice: ")

    if option == '1':
        add_product()
    elif option == '2':
        product_id = input("Enter the product ID to remove: ")
        remove_product(product_id)
    elif option == '3':
        product_id = input("Enter the product ID to update: ")
        field = input("Enter the field to update (name, description, price, stock): ")
        new_value = input("Enter the new value: ")
        update_product(product_id, field, new_value)
    elif option == '4':
        display_products()
    elif option == '5':
        lowest_price_product_id = find_product_with_lowest_price(products)
        if lowest_price_product_id:
            print(f"Product with the lowest price: {lowest_price_product_id}")
        else:
            print("No products found.")
    elif option == '6':
        break
    else:
        print("Invalid option. Please select a valid option.")

Q. You work for a social media company and have been tasked with analyzing user engagement on the platform. You have been given a dataset of 
user interactions for the past month, which includes information such as user ID, post ID, timestamp, and type of interaction (e.g. like, comment, share).
Your goal is to create a report that summarizes the user engagement on the platform. Specifically, you need to calculate the total number of interactions 
  for each user and for each post, and also identify the most popular posts based on the number of interactions they received.
import pandas as pd

data = [
    {'user_id': 1, 'post_id': 101, 'timestamp': '2023-01-01 12:00:00', 'interaction_type': 'like'},
    {'user_id': 2, 'post_id': 101, 'timestamp': '2023-01-01 12:15:00', 'interaction_type': 'comment'},
    {'user_id': 3, 'post_id': 101, 'timestamp': '2023-01-01 12:30:00', 'interaction_type': 'share'},
    {'user_id': 1, 'post_id': 102, 'timestamp': '2023-01-01 12:05:00', 'interaction_type': 'like'},
    {'user_id': 2, 'post_id': 102, 'timestamp': '2023-01-01 12:10:00', 'interaction_type': 'like'},
    {'user_id': 3, 'post_id': 102, 'timestamp': '2023-01-01 12:15:00', 'interaction_type': 'comment'},
]

df = pd.DataFrame(data)

user_interactions = df.groupby('user_id')['interaction_type'].count().reset_index()
user_interactions.columns = ['user_id', 'total_interactions']

post_interactions = df.groupby('post_id')['interaction_type'].count().reset_index()
post_interactions.columns = ['post_id', 'total_interactions']

most_popular_posts = post_interactions.sort_values(by='total_interactions', ascending=False)

print("User Interactions:")
print(user_interactions)

print("\nPost Interactions:")
print(post_interactions)

print("\nMost Popular Posts:")
print(most_popular_posts)
