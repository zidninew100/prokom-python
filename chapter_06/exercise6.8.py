
hewan_1 = {
    "jenis": "Kucing",
    "pemilik": "Muhammad"
}

hewan_2 = {
    "jenis": "Anjing",
    "pemilik": "Ahmad"
}

hewan_3 = {
    "jenis": "Kelinci",
    "pemilik": "Mohamad"
}

pets = [hewan_1, hewan_2, hewan_3]

for hewan in pets:
    print("\nInformasi hewan:")
    for key, value in hewan.items():
        print(f"{key}: {value}")
