
while True:
    umur = input(
        "Masukkan umur (ketik 'quit' untuk selesai): "
    )

    if umur == "quit":
        break

    umur = int(umur)

    if umur < 3:
        print("Tiket gratis.")
    elif umur <= 12:
        print("Harga tiket Rp10.")
    else:
        print("Harga tiket Rp15.")
