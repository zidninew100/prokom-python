
bahasa_favorit = {
    "Muhammad": "Python",
    "Ahmad": "Java",
    "Mohamad": "C++"
}

peserta_polling = [
    "Muhammad",
    "Ahmad",
    "Mohamad",
    "Zidni",
    "Agus"
]

for nama in peserta_polling:
    if nama in bahasa_favorit:
        print(f"Terima kasih, {nama}, sudah mengisi polling.")
    else:
        print(f"{nama}, silakan ikut mengisi polling.")
