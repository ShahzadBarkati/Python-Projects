import random 

print("Welcome to Word Scrambler!")
print("__________________________________")

while True: 
  word = input("Enter a single word to scamble ( or 'exit' to quit):  ")

  if word.lower() == 'exit':
    print("Good Bye...")
    break

  letters = list(word)
  random.shuffle(letters)

  print(f"Scrambled word: {"".join(letters)}")

print("__________________________________")
print("Thank you.....")
print("__________________________________")