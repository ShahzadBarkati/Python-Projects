import random

print("Welcome to the Recipe Generator App")
print("_______________________________________")

proteins = ["beef", "chiken", "fish", "mutton", "eggs"]
veggies = ["broccoli", "carrots", "mushroom", "spinach"]
carbs = ["rice", "pasta", "potato", "bread"]
methods = ["baked", "grilled", "stir-fired", "rosted"]
flavors = ["garlic", "lemon", "spicy", "herb", "sweet & sour"]


while True:
  protein = random.choice(proteins)
  veggie = random.choice(veggies)
  carb = random.choice(carbs)
  method = random.choice(methods)
  flavor = random.choice(flavors)

  # formula   [flavor] [method] [protein] with [veggie] [carb]
  print(f"\nYour random recipe: [ {flavor.title()} {method} { protein} with { veggie} { carb} ]")

  if not input("\nWant to generate another recipe? (y/n): ").lower().startswith('y'):
    print("Good bye...")
    break