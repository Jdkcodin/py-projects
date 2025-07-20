import random
print("Random Recipe Generator")

proteins = ["chicken breast", "ground beef", "tofu", "salmon", "shrimp", "turkey","pork loin", "egg", 
"lamb chops", "tempeh", "cod","chickpeas", "lentils"]

veggies = ["broccoli", "spinach", "carrots", "bell peppers", "zucchini", "asparagus","cauliflower",
"green beans", "mushrooms", "kale", "cabbage", "onion", "garlic"]

methods = ["grilled", "baked", "roasted", "stir-fried", "steamed", "pan-seared","slow-cooked", "braised", 
"poached", "blanched", "air-fried"]

carbs = ["rice", "pasta", "quinoa", "couscous", "bread", "sweet potato", 
"potato", "noodles", "tortilla", "polenta", "barley", "bulgur"]

flavours = ["spicy", "savory", "sweet", "tangy", "herby", "smoky", "umami", 
"citrusy", "garlicky", "peppery", "earthy", "zesty"]

while True:
    flavour= random.choice(flavours)
    protein = random.choice(proteins)
    veggie = random.choice(veggies)
    method= random.choice(methods)
    carb = random.choice(carbs)
    print(f"Your Random recipe is :{flavour} {method} {protein} with {veggie} and {carb}")

    if not input("Generate another one?? (Y/n) :").lower().startswith("y"):
        print("GOODBYE")
        break


