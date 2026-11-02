guests = ["Muhammad", "Ahmad", "Mohamad"]

print("Mohamad tidak bisa hadir ke acara makan malam.")

guests[2] = "Agus"

print("Daftar tamu terbaru:")
print(guests)

for guest in guests:
    print(f"Halo {guest}, saya mengundang kamu untuk makan malam hari Sabtu!")