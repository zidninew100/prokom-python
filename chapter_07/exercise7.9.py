
sandwich_orders = [
    "tuna",
    "pastrami",
    "ayam",
    "pastrami",
    "keju",
    "pastrami",
    "telur"
]

finished_sandwiches = []

print("Maaf, stok pastrami sedang habis.")

while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")

while sandwich_orders:
    sandwich = sandwich_orders.pop()

    print(f"Sandwich {sandwich} sudah dibuat.")
    finished_sandwiches.append(sandwich)

print("\nSandwich yang sudah dibuat:")
for sandwich in finished_sandwiches:
    print(f"- {sandwich}")
