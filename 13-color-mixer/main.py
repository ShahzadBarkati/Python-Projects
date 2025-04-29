
print("Welcome to the Color Mixer App")
print("_______________________________________")

color_mixes = {
  ("red", "blue"): "purple",
  ("red", "yellow"): "orange",
  ("yellow", "blue"): "green",
  ("green", "blue"): "teal",
  ("red", "white"): "pink",
  ("red", "green"): "brrown",
}

while True: 
  color1 = input("\nEnter first color: ").lower().strip()
  color2 = input("Enter second color: ").lower().strip()

  mix = None

  if (color1, color2) in color_mixes:
    mix = color_mixes[(color1, color2)]
  elif (color2, color1) in color_mixes:
    mix = color_mixes[(color2, color1)]

  if mix:
    print(f"When you mix {color1} and {color2}, you get the {mix}!")
  else: 
    print("I don't know the mixer of these color...")

  if not input("\nWant to mix more colors? (y/n): ").lower().startswith('y'):
    print("Good bye...")
    break
