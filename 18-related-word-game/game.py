import random
import time

word_pairs = {
  "sky": ["sun", "blue", "cloud", "fly", "bird"],
  "water": ["drink", "swim", "fish", "boat", "occean"],
  "food": ["eat", "cook", "tasty", "meal", "restaurant"],
  "music": ["listen", "song", "dance", "band", "rhythm"],
  "book": ["cover", "read", "story", "page", "author", "library"],
  "tree": ["leaf", "wood", "forest", "green", "shade"],
  "car": ["road", "wheel", "travel", "speed", "drive"],
  "dog": ["pet", "bark", "loyal", "walk", "puppy"],
}

print("\nWelcome to the Related Word Game!")
print("________________________________________")

score = 0
round = 0

while True: 

  prompt = random.choice(list(word_pairs.keys()))
  related_words = word_pairs[prompt]

  print(f"\nPrompt word: {prompt.upper()}")
  print("Quick type a word related to this in your mind come first: ")

  # start timer  - current time
  start_time = time.time()

  # make user input in lower case as well remove white spaces
  response = input("> ").lower().strip()

  # calculating response time
  response_time = time.time() - start_time

  if response in related_words:
    points = max(1, 5, int(response_time))
    score += points
    print(f"\nGood association!! +{points} pionts (answered in {response_time:.1f} sec)")
  else:
    print(f"Not a common association. Related word includes: {", ".join(related_words)}")

  round += 1
  print(f"Score: {score}/{score * 5} possible points")

  if input("\nDo you want to play again? (Y/N) ").lower().startswith('n'):
    print(f"Final score: {score}. Thank You!!")
    break