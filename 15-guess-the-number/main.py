import random 

print("Welcome to the Guess the Number Game")
print("_______________________________________")

min = 1
max = 50
max_attempt = 5
num_of_attempt = 1

print(f"\nI'm thinking of a number between {min} to {max}. You have {max_attempt} attempt to guess the correct number!")

num = random.randint(min, max)

print(num)

while True:
  try: 
    guess = int(input(f"\nAttempt {num_of_attempt}/{max_attempt}. Enter your guess: "))
  
  except ValueError:
    print(f"\nPlease enter a valid number between {min} to {max}")
    continue

  num_of_attempt += 1

  if guess == num:
    print(f"\nHurry! You guees the correct number: {num}\n")
    print("_______________________________________\n")
    break

  if num_of_attempt > max_attempt:
    print(f"\nSorry, your max guess attempt '{max_attempt}' is over. Better luck next time...\n")
    break
