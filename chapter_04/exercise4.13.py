foods = ("fried rice", "fried chicken", "noodles", "satay", "meatballs")

print("Menu awal restoran:")
for food in foods:
    print(food)

print("\nMencoba mengubah salah satu menu:")

try:
    foods[0] = "pizza"
except TypeError:
    print("Python menolak perubahan karena tuple tidak bisa diubah.")

foods = ("pizza", "burger", "noodles", "satay", "meatballs")

print("\nMenu restoran yang baru:")
for food in foods:
    print(food)