nums = [1,2,3,4,5]

print(nums)
print(*nums)  # Unpacking the list

def orderPizza(size, *toppings):
    print(f"Pizza size: {size}")
    print(f"Number of toppings: {len(toppings)}")
    print("Toppings ordered:")
    for topping in toppings:
        print(f"- {topping}")

orderPizza("Large", "Pepperoni", "Mushrooms", "Onions", "Extra cheese")

def orderPizza(size, *toppings, **details):
    print(f"ordered pizza size: {size}, with toppings: {toppings} and details: {details}")    

orderPizza("Large", "Pepperoni", "Mushrooms", "Onions", "Extra cheese", Delivery="Yes", Address="123 Main St")
