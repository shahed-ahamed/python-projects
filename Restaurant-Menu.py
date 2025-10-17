
menu = {
    'pizza': 300,
    'burger': 150,
    'pasta': 250,
    'salad': 100,
    'soda': 50,
    'coffee': 80,
}
print("Welcome to the Hotel Menu!")
print("Here is our menu:")
print("Pizza - 300TK")
print("Burger - 150TK")   
print("Pasta - 250TK")
print("Salad - 100TK")
print("Soda - 50TK")
print("Coffee - 80TK")
 
order_total = 0

item_1 =input("Enter the first item you want to order: ")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"{item_1} added to your order. Price: {menu[item_1]}TK")
    
else:
    print(f"Sorry, {item_1} is not on the menu.")
    
another_order = input("Do you want to order another item? (yes/no): ")

if another_order == 'yes':
    item_2 = input("Enter the second item you want to order: ")
    print(f"You have ordered: {item_1} and {item_2}")
else:
    print(f"You have ordered: {item_1}")
    
print(f"Your total order amount is: {order_total}TK")
