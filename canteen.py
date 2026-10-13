menu = {
    "idli": 30,
    "dosa": 50,
    "tea": 25,
    "coffee": 20,
    "samosa": 15,
    "juice": 40,
    "lemon Rice":20,
    "sambar": 15,
    "chutney":47
}

print("Welcome to the Canteen!")

for item, price in menu.items():
    print(f"{item}: ₹{price}")
