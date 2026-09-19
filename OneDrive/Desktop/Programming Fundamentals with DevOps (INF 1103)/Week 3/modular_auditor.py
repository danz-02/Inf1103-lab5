##Set inventory to '0'
inventory=0

def get_valid_input():
    user_input= input("Enter a stock quantity: ")

    if user_input == "quit":
        print("Exiting the program...")
        return None
        
         ##Check for valid-input
    elif user_input.isdigit():
        return int(user_input)
        
    else:
        print("Invaild input.. Please try again or 'quit'")
        return get_valid_input()
        

def process_delivery():
   stock_count = get_valid_input()
   new_total= inventory+ stock_count
   print(f"New Total Delivery: {new_total} ")


#def calculate_tax(amount)




#print("\n Final Inventory Report")
#print(f"Total Units Processed (Final Stock): {inventory}")
