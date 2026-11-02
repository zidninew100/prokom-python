
angka_favorit = {
    "Zidni": [23, 10, 15],
    "Muhammad": [5, 8],
    "Ahmad": [12, 20],
    "Mohamad": [3, 9],
    "Agus": [6, 11, 18]
}

for nama, angka in angka_favorit.items():
    print(f"\nAngka favorit {nama}:")
    for nomor in angka:
        print(f"- {nomor}")
