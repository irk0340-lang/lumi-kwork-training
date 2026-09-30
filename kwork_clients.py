clients = [
    {"name": "Иван", "phone": "111"},
    {"name": "Олег", "phone": "222"},
    {"name": "Анна", "phone": "333"}
]

for client in clients:
    if client["phone"][0] == "2":
        print("Подходит", client["name"], "-", client["phone"])