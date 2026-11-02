cities = ["Jakarta", "Bandung", "Surabaya"]

print("Mencoba mengakses indeks yang salah:")

try:
    print(cities[3])
except IndexError:
    print("Terjadi IndexError karena indeks tersebut tidak tersedia.")

print("\nMengakses indeks yang benar:")
print(cities[2])