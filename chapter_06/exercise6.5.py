
sungai = {
    "nil": "mesir",
    "amazon": "brasil",
    "gangga": "india"
}

for nama_sungai, negara in sungai.items():
    print(
        f"Sungai {nama_sungai.title()} mengalir "
        f"melalui {negara.title()}."
    )

print("\nDaftar nama sungai:")
for nama_sungai in sungai.keys():
    print(nama_sungai.title())

print("\nDaftar negara:")
for negara in sungai.values():
    print(negara.title())
