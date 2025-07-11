
total_bill = 0

def add_items(*prices):
    global total_bill
    total_bill += sum(prices)

def get_total():
    global total_bill
    return total_bill

def apply_discount(percent):
    global total_bill
    discount = total_bill * (percent / 100)
    total_bill -= discount
    return total_bill

add_items(10, 5, 3)       
print("Total:", get_total())  

apply_discount(10)       
print("Total after discount:", get_total())  
