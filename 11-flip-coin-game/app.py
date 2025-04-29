import random

print("Welcome to the Flip Coin Game")
print("_______________________________________________")

while True:
  choice  = input("\nEnter you guess: [ Heads / Tails]: ").lower()

  if choice != 'heads' and choice != 'tails': 
    print("Please enter H for heads and T for tails.")
    continue

  flip = random.choice(["heads","tails"])
  print(f"\nChoice shows: {flip.capitalize()}")

  if choice == flip:
    print("\nYou won!!")
  else: 
    print("\nSorry, wrong guess.")
  
  again = input("\nPlay again? (Y / N): ")
  if again.lower() == 'n':
    print("Good Bye...")
    break
  else:
    continue

  