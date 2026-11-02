places = ["Jepang", "Madinah", "Swiss", "Korea Selatan", "Turki"]

print("Daftar tempat:")
print(places)

print("\nDaftar berdasarkan urutan alfabet:")
print(sorted(places))

print("\nDaftar berdasarkan urutan alfabet terbalik:")
print(sorted(places, reverse=True))

print("\nDaftar asli:")
print(places)

places.reverse()
print("\nDaftar setelah reverse():")
print(places)

places.reverse()
print("\nDaftar setelah reverse() kedua:")
print(places)

places.sort()
print("\nDaftar setelah sort():")
print(places)

places.sort(reverse=True)
print("\nDaftar setelah sort(reverse=True):")
print(places)