nama = "Zidni"
umur = 19
makanan = ["nasi goreng", "ayam goreng", "bakso"]

# Pengujian kesamaan dan ketidaksamaan
print(nama == "Zidni")
print(nama == "zidni")

# Pengujian menggunakan lower()
print(nama.lower() == "zidni")

# Pengujian angka
print(umur == 19)
print(umur != 20)
print(umur > 17)
print(umur < 25)

# Pengujian menggunakan and dan or
print(umur > 17 and umur < 25)
print(umur < 17 or umur > 18)

# Pengujian keanggotaan list
print("bakso" in makanan)
print("sate" not in makanan)