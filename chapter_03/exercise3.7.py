guests = ["Fajar", "Muhammad", "Nadia", "Ahmad", "Agus", "Rafi"]

print("Maaf, meja makan yang baru tidak bisa tiba tepat waktu.")
print("Saya hanya bisa mengundang dua orang.")

while len(guests) > 2:
    removed_guest = guests.pop()
    print(f"Maaf {removed_guest}, saya tidak bisa mengundang kamu kali ini.")

for guest in guests:
    print(f"Halo {guest}, kamu tetap diundang untuk makan malam!")

del guests[0]
del guests[0]

print("Daftar tamu terakhir:")
print(guests)