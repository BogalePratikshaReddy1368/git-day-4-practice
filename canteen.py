menu = {
    "idli": 30,
    "dosa": 50,
    "tea": 15,
    "coffee": 20
}

print("Welcome to the Canteen!")

for item, price in menu.items():
    print(f"{item}: ₹{price}")