import random

print("Welcome to the Guess the Word Game")
print("_______________________________________")

words = ["python", "php", "code", "learn", "fun", "enjoy", "game", "computer"]

while True:
  
  original_word = random.choice(words)
  letters = list(original_word)
  random.shuffle(letters)

  print(f"\nScrambled word: {''.join(letters)}")

  guess_word = input("\nGuess the correct word: ").lower().strip()

  if original_word == guess_word:
    print("\nHurry, You guess the correct word!!")
  else:
    print(f"\nSorry, wrong guess. Correct word is >> '{original_word}'")

  if not input("\nPlay again? (y/n)").lower().strip().startswith("y"):
    print("Thank you!")
    break
