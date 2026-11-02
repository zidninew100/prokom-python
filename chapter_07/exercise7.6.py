
# Cara 1: Kondisi pada while
topping = ""

while topping != "quit":
    topping = input("Masukkan topping (quit untuk selesai): ")

    if topping != "quit":
        print(f"Topping {topping} ditambahkan.")


# Cara 2: Menggunakan active flag
aktif = True

while aktif:
    topping = input("Masukkan topping (quit untuk selesai): ")

    if topping == "quit":
        aktif = False
    else:
        print(f"Topping {topping} ditambahkan.")


# Cara 3: Menggunakan break
while True:
    topping = input("Masukkan topping (quit untuk selesai): ")

    if topping == "quit":
        break

    print(f"Topping {topping} ditambahkan.")
