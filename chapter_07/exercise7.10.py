
hasil_polling = {}

while True:
    nama = input("Siapa nama kamu? ")
    tempat = input(
        "Jika bisa berlibur ke mana saja, kamu ingin ke mana? "
    )

    hasil_polling[nama] = tempat

    lanjut = input("Apakah ada peserta lain? (ya/tidak): ")

    if lanjut.lower() != "ya":
        break

print("\n--- Hasil Polling Liburan Impian ---")

for nama, tempat in hasil_polling.items():
    print(f"{nama} ingin berlibur ke {tempat}.")
