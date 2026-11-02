
pengguna = {
    "nama": "Zidni",
    "umur": 19,
    "kota": "Cilacap",
    "hobi": ["Bermain game", "Belajar Python"],
    "bahasa_pemrograman": ["Python", "Java"]
}

print("Profil Pengguna")
print(f"Nama: {pengguna['nama']}")
print(f"Umur: {pengguna['umur']} tahun")
print(f"Kota: {pengguna['kota']}")

print("\nHobi:")
for hobi in pengguna["hobi"]:
    print(f"- {hobi}")

print("\nBahasa pemrograman yang dipelajari:")
for bahasa in pengguna["bahasa_pemrograman"]:
    print(f"- {bahasa}")
