
def make_sandwich(*items):
    print("\nPesanan sandwich:")
    for item in items:
        print(f"- {item}")

    print("Sandwich sedang disiapkan!")


make_sandwich("ayam")
make_sandwich("keju", "telur")
make_sandwich("daging", "selada", "tomat", "keju")
