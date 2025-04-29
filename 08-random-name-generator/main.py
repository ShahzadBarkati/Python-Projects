import random

print("Welcome to the Fantancy Random Name Generator")
print("_______________________________________________")

first_name = ["John", "Sky", "Moon", "Ice", "Fire", "Sun"]
last_name = ["Doe", "Rider", "Walker", "Singer", "Dancer", "Hunter"]

count = int(input("How many random names you want? "))

for i in range(count): 
  first = random.choice(first_name)
  last = random.choice(last_name)

  print(f"{first} {last}")