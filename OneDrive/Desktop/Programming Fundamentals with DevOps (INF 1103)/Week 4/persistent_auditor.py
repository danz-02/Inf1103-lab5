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
