
kegiatan = ["Belajar Python", "Mengerjakan tugas", "Membaca buku"]

print("Daftar Kegiatan Hari Ini:")
for aktivitas in kegiatan:
    print(f"- {aktivitas}")

pilihan = input("Apakah lo ingin menambah kegiatan? (ya/tidak): ")

if pilihan.lower() == "ya":
    kegiatan_baru = input("Masukkan kegiatan baru: ")
    kegiatan.append(kegiatan_baru)

    print("\nDaftar kegiatan terbaru:")
    for aktivitas in kegiatan:
        print(f"- {aktivitas}")
else:
    print("Tidak ada kegiatan yang ditambahkan.")
