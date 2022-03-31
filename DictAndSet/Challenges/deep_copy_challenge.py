from contents import recipes

def deep_copy(old_dictionary: dict) -> dict:
    """Take a dictionary without lists or tuples, and return a deepcopy version"""
    new_dictionary = {}
    for key, value in old_dictionary.items():
        new_value = value.copy()
        new_dictionary[key] = new_value

    return new_dictionary


recipes_copy = deep_copy(recipes)
recipes_copy["Butter chicken"]["ginger"] = 300
print(recipes_copy["Butter chicken"]["ginger"])
print(recipes["Butter chicken"]["ginger"])
