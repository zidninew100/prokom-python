
sandwich_orders = [
    "tuna",
    "ayam",
    "keju",
    "telur"
]

finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()

    print(f"Saya sudah membuat sandwich {sandwich}.")
    finished_sandwiches.append(sandwich)

print("\nSandwich yang sudah dibuat:")
for sandwich in finished_sandwiches:
    print(f"- {sandwich}")
