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

def save_inventory(orders):
    ##Append new transactions to "orders.json", using "a" mode
    f=open("inventory.json", "a")
    with open("inventory.json", "w") as f:
        json.dump(orders, f)


def display_all():

    print("--------MENU--------")
    
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit")

    print("--------------------")


def update_stock(stocks):

    print("Update Stock")
    search_id = input("Enter Product ID: ")

    ##Search for product id then update stock
    for stock in stocks:
        if stock["id"] == search_id:

            print("Product Found: ")
            print("Name: ", stock["name"])
            print("Current Stock: ",stock["stock_quantity"])

    new_stock = input("New Stock Quantity: ")
    stock["stock_quantity"] = new_stock

    print("New Stock Quantity [new_stock]")
    print("Stock updated successfully! ")
    return stocks
        

def search_product(stocks):

    print("Search Product")
    search_id = input("Enter Product ID: ")
    ##Search for product id then search for list of stock

    for stock in stocks:
        if stock["id"] == search_id:

            print("Product Found:")
            print("Name:", stock["name"])
            print("Stock:", stock["stock_quantity"])

        else: 
            print("Product not found.")

orders = load_inventory()
display_all()

while True:

    menu_option = input("Enter your choice: ")

    if menu_option == "1":
        print("Current Inventory: ")
        display(orders)

    elif menu_option == "2":
        print("Add Product/n")
        orders= add_product(orders)

    elif menu_option == "3":
        print("Update Product/n")
        orders= update_stock(orders)

    elif menu_option == "4":
        print("Search Product/n")
        orders= search_product(orders)

    elif menu_option == "5":
        print("Save Inventory")
        save_inventory(orders)

    elif menu_option == "6":
        print("Saving inventory before exit.../n Inventory saved successfully. ")
        print("Thank you for using Inventory Management System. Program terminated.")
        break
    else:
        print("Invalid choice.. Please try again")
