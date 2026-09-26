import os
import sys

def get_valid_input():
    user_input= input("Enter a stock quantity: ")
    ##Reusing last week code to prompt user for stock quantity
    if user_input == "quit":
        print("Exiting the program...")
        return None
        
         ##Check for valid-input
    elif user_input.isdigit():
        ##Checking numeric inputs
        return int(user_input)
        
    else:
        print("Invaild input.. Please try again or 'quit'")
        return "Invaild"

def load_inventory():
    ##Load previous transaction history
    orders = []
    if os.path.exists("orders.txt"):
        f=open("orders.txt","r")
        for line in f:
            line = line.strip()
            if not line: continue
            num =line.split(",", 2)
            if len(num) !=3: continue
            id, name, qty = num  ##Ensure id, name, qty is in the correct format
            if id.isdigit() and qty.strip().isdigit():
                orders.append([id, name.strip(), int(qty)])
        f.close()
    else:
        ##No previous records, will automatically create a new file 
        f=open("order10.txt", "w")
        f.close()
    return orders

def save_inventory(new_input):
    ##Append new transactions to "orders.txt, using "a" mode
    f=open("orders.txt", "a")
    f.write(f"{new_input[0]},{new_input[1]},{new_input[2]}\n ")
    f.close()

def get_next_id(orders):
    ##For the next increment order ID
    if len(orders) == 0:
        return 1001
    ##Initialise "1001" as the start order ID as shown from the lab

    return max(order[0] for order in orders) + 1

orders=load_inventory()
print("Current Orders:\n")


if not orders:
    print("No current orders.. Creating a new file")
else:
    for o in orders:
        print(f"{o[0]}, {o[1]}, {o[2]}")

        
while True:

    ##Prompt user to enter a product
    product_name= input("Enter a product: ")
    ##When user enter 'quit' programme will save the records
    if product_name =="quit":
        save_inventory(orders)
        print("Current Orders")
    else:
         for o in orders:
                print(f"{o[0]}, {o[1]}, {o[2]}")

    ##Prompt user to a vaild product quantity value, else program exit
    qty ="Invalid"
    while qty =="Invalid":
        qty= get_valid_input()
        if qty is None:
            save_inventory(orders)
            sys.exit()

    ##Incrementing order id and save 'order' into the list
    new_id = get_next_id(orders)

    new_order = [new_id, product_name, qty] 
    orders.append(new_order)

    ##Add new order into the list
    save_inventory(new_order) 

    ##Print statement whenever an item is added 
    print("New Order Added:")
    print(f"{new_order[0]}, {new_order[1]}, {new_order[2]}")
    print("Order successfully saved to orders.txt")
