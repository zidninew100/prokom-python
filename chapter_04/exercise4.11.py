my_pizzas = ["pepperoni", "cheese", "chicken"]

friend_pizzas = my_pizzas[:]

my_pizzas.append("mushroom")
friend_pizzas.append("beef")

print("My favorite pizzas are:")
for pizza in my_pizzas:
    print(pizza)

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)