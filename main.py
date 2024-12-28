#Concession Stand Program

menu = {
    "pizza": 3.0,
    "nachos": 4.5,
    "popcorn": 6.0,
    "fries": 2.5,
    "chips": 1.0,
    "pretzel": 3.5,
    "soda": 3.0,
    "lemonade": 4.25
}

cart = []
total = 0

print("------- MENU --------")
for key, value in menu.items():
    print(f"{key:10}: {value:.2f}")
print("---------------------")

while True:
    food = input("Select an item (q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

print("------- YOUR ORDER --------")
for food in cart:
    total += menu.get(food)
    print(food, end = " ")

print()
print(f"Total is ${total:.2f}")