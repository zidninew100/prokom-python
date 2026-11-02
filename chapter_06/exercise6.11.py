
cities = {
    "surakarta": {
        "country": "Indonesia",
        "population": 522000,
        "fact": "Dikenal sebagai Kota Batik."
    },
    "tokyo": {
        "country": "Jepang",
        "population": 14000000,
        "fact": "Merupakan ibu kota Jepang."
    },
    "paris": {
        "country": "Prancis",
        "population": 2100000,
        "fact": "Terkenal dengan Menara Eiffel."
    }
}

for nama_kota, informasi in cities.items():
    print(f"\nKota: {nama_kota.title()}")
    print(f"Negara: {informasi['country']}")
    print(f"Populasi: {informasi['population']}")
    print(f"Fakta: {informasi['fact']}")
