cities = ["Jakarta", "Bandung", "Surabaya", "Yogyakarta", "Solo"]

print("Daftar kota:")
print(cities)

print("\nJumlah kota:")
print(len(cities))

print("\nMengakses elemen berdasarkan indeks:")
print(cities[0])

print("\nMengubah elemen:")
cities[1] = "Malang"
print(cities)

print("\nMenambahkan elemen dengan append():")
cities.append("Semarang")
print(cities)

print("\nMenyisipkan elemen dengan insert():")
cities.insert(1, "Bogor")
print(cities)

print("\nMenghapus elemen dengan del:")
del cities[0]
print(cities)

print("\nMenghapus elemen dengan pop():")
popped_city = cities.pop()
print(cities)
print(f"Kota yang dihapus: {popped_city}")

print("\nMenghapus elemen dengan remove():")
cities.remove("Malang")
print(cities)

print("\nMengurutkan daftar dengan sorted():")
print(sorted(cities))

print("\nMengurutkan daftar secara permanen dengan sort():")
cities.sort()
print(cities)

print("\nMembalik urutan daftar dengan reverse():")
cities.reverse()
print(cities)