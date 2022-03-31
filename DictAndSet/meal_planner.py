from contents import pantry, recipes


def add_to_cart(data: dict, item: int, quantity: int) -> None:
    """Adds quantity of an item needed for recipes selected."""
    # current_amt = data.pop(item, 0)
    # data[item] = (current_amt + quantity)

    # This is the same as the setdefault for dictionaries.
    # if item in data:
    #     data[item] += quantity
    # else:
    #     data[item] = quantity
    data[item] = data.setdefault(item, 0) + quantity


# display_dict = {str(index + 1): meal for index, meal in enumerate(recipes)}
display_dict = {}
for index, key in enumerate(recipes):
    display_dict[str(index + 1)] = key

shopping_cart = {}

while True:
    # Display a menu of the receipes we know how to cook
    print("Please choose your recipe")
    print("-------------------------")
    for key, value in display_dict.items():
        print(f"{key} - {value}")

    choice = input(": ")
    if choice == "0":
        break
    elif choice in display_dict:
        selected_item = display_dict[choice]
        print(f"\nyou have selected {selected_item}\n")
        print("checking ingredients")
        print(recipes[selected_item])
        for ingredient, required_quantity in recipes[selected_item].items():
            # passing back a value of zero if not exists
            quantity_in_pantry = pantry.get(ingredient, 0)
            if required_quantity > quantity_in_pantry:
                print(f"\tYou don't have enough {ingredient} in the pantry.  {required_quantity - quantity_in_pantry}"
                      f" short.")
                add_to_cart(shopping_cart, ingredient, required_quantity - quantity_in_pantry)

for items in sorted(shopping_cart):
    print(f"{items}: {shopping_cart[items]}")

