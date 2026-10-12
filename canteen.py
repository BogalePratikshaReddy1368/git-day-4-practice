menu = {
    "idli": 30,
    "dosa": 50,
    "tea": 20,
    "coffee": 20,
    "samosa": 15,
    "juice": 40,
    "lemon Rice":50
}

print("Welcome to the Canteen!")

for item, price in menu.items():
    print(f"{item}: ₹{price}")