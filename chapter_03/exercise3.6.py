guests = ["Muhammad", "Ahmad", "Agus"]

print("Saya menemukan meja makan yang lebih besar!")

guests.insert(0, "Fajar")
guests.insert(2, "Nadia")
guests.append("Rafi")

for guest in guests:
    print(f"Halo {guest}, saya mengundang kamu untuk makan malam hari Sabtu!")