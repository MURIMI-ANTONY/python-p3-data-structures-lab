spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    return [x.get("name") for x in spicy_foods]

def get_spiciest_foods(spicy_foods):
    return [item for item in spicy_foods if item["heat_level"] >5 ]

def print_spicy_foods(spicy_foods):
    output = "\n".join([f"{x.get('name')} ({x.get('cuisine')}) | Heat Level: {'🌶' * x.get('heat_level')}" for x in spicy_foods])
    print(output)  # Add this line to print the actual output
    return output


def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    matching_foods = [x for x in spicy_foods if x.get("cuisine") == cuisine]
    return matching_foods[0] if matching_foods else None

def print_spiciest_foods(spicy_foods):
    output= "\n".join([f"{x.get('name')} ({x.get('cuisine')}) | Heat Level: {'🌶' * x.get('heat_level')}" for x in spicy_foods if x.get("heat_level")>5])
    print(output)

def get_average_heat_level(spicy_foods):
    return sum(x.get("heat_level") for x in spicy_foods)// len(spicy_foods)

def create_spicy_food(spicy_foods, spicy_food):
     updated_spicy_foods = spicy_foods.copy()
    # Add the new spicy_food to the copy
     updated_spicy_foods.append(spicy_food)
     return updated_spicy_foods
