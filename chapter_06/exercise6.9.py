
favorite_places = {
    "Zidni": ["Bali", "Yogyakarta"],
    "Muhammad": ["Jakarta", "Bandung"],
    "Ahmad": ["Surakarta", "Malang"]
}

for nama, tempat in favorite_places.items():
    print(f"\nTempat favorit {nama}:")
    for lokasi in tempat:
        print(f"- {lokasi}")
