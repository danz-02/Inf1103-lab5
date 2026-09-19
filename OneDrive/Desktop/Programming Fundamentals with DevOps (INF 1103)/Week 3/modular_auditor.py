##Set inventory to '0'
inventory=0
failed_entries=0

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
        return "Invaild"

def process_delivery(current_total, new_value):
   new_total= current_total+ new_value
   print(f"New Total Delivery: {new_total} ")
   return new_total

def calculate_tax(amount):
    tax_amount= amount*0.10
    print(f"Tax amount {tax_amount}")
    return tax_amount
