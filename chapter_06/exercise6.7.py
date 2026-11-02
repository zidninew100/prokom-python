
orang_1 = {
    "first_name": "Muhammad",
    "last_name": "Ahmad",
    "age": 20,
    "city": "Surakarta"
}

orang_2 = {
    "first_name": "Ahmad",
    "last_name": "Agus",
    "age": 21,
    "city": "Jakarta"
}

orang_3 = {
    "first_name": "Mohamad",
    "last_name": "Fajar",
    "age": 19,
    "city": "Yogyakarta"
}

people = [orang_1, orang_2, orang_3]

for orang in people:
    print("\nInformasi orang:")
    for key, value in orang.items():
        print(f"{key}: {value}")
