import os
import json

def add_product(orders):
    name= input("Enter a product: ")
    ##Reusing last week code to prompt user for stock quantity
    id = input("Enter an ID: ")
    price = input("Enter the price: ")
    stock_quantity = input("Enter a stock quantity: ")

    product={"id": id, "name": name, "price" : price, "stock_quantity": stock_quantity}
    orders.append(product) ##Dictionary of products

    print("Product added successfully! ")
    return orders

def load_inventory():
    ##Load previous transaction history
    orders = []
    if os.path.exists("inventory.json"):
        try:
            with open("inventory.json", "r") as file:
                orders = json.load(file)
        except json.JSONDecodeError:
            orders=[]
        print("inventory.json found.\n Inventory loaded successfully. ")

    else:
        ##No previous records, will automatically create a new file 
        order=[]
        f=open("inventory.json", "w")
        f.close()
    return orders

def display(orders):

    print("\nCurrent Inventory\n" "--------------------------------------------")
    for product in orders:
        print(" | ".join(f"{key}: {value}" for key, value in product.items()))
    print("--------------------------------------------\n") ##Display 


