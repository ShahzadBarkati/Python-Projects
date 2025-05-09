import random
import time
import os

print("Welcome to the Memory Sequence Game!!")
print("________________________________________")


def clear_screen():
  ''' Clear the terminal screen '''
  os.system("cls" if os.name == 'nt' else "clear")

print("*** Remember the Sequence of the number and type it back in correct sequence ***")
print("----- RULES ------")
print("- Watch as the number appears one by one")
print("- After the sequence is shown type it back in correct order")
print("- Each round add one more number to remember")
print("- Let's see, how far can you go....")

print("Press enter to start the game...")


sequence = []
current_round = 1
game_over = False

while not game_over:
  sequence.append(random.randint(1,9))

  clear_screen()

  print(f"\n +++++ Round {current_round} ++++++")
  print(f"Remember this sequence of {len(sequence)} numbers...")

  for number in sequence:
    time.sleep(0.7)
    print(f"{number}")
    time.sleep(0.8)
    clear_screen()

  print("\nNow repeat the sequence by typing each number, seperated by space.")
  answer = input("> ")

  try:
    player_sequence = [int(num) for num in answer.split()]

  except ValueError:
    print("Please enter number only.")
    game_over = True
    continue


  if player_sequence == sequence:
    print(f"\nCongrates, You remember all {len(sequence)} numbers")
    current_round += 1
    time.sleep(2)
  else:
    print(f"\nGame over! You remmeber all {current_round - 1} numbers!")
    print(f"Correct sequence: {" ".join(str(num) for num in sequence)}")
    game_over = True

  if game_over: 
    if not input("\nDo you want to play again? (Y/N)  ").lower().startswith('y'):
      print("Good bye...")
      break
    else:
      sequence = []
      current_round = 1
      game_over = False