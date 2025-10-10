##concession stand program
menu = {"pizza" : 189,
        "burger" : 199,
        "soda" : 99,
        "coke" : 129,
        "chips" : 89,
        "fries" : 79}

cart = []
total =0
qty = 0
print("----------MENU----------")
print("\nITEMS       PRICE")
for key , value in menu.items():
    print(f"{key:10} : {value:.2f}")
    
print("Please select your prefer items : ")

while True:
    food = input("Item: ").lower()
    if food == "q":
        print("THANK YOU!")
        break
    elif food in menu:
        cart.append(food)
        print(f"Added '{food}' to your cart.")
    else:
        print(f"'{food}' not found in menu. Please try again.")
print("-----Your Cart-----")
items_counts = {}
for food in cart:
    if food not in items_counts:
        items_counts[food] = 0
    items_counts[food] += 1  
        
print("\n ITEMS       QTY     PRICE      SUBTOTAL")
for food,qty in items_counts.items() :
    price = menu.get(food)
    total += menu.get(food)
    subtotal = qty * price
    print(f" {food:10}  {qty:1}      {price:.2f}       {subtotal:.2f}")
    
print()   
print("-------------------------")     
print(f"Total is : {total:.2f}")
print("-------------------------")