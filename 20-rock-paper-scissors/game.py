import random
import time

def display_welcome():
  print("Welcome to the Rock-Paper-Scissors Game")
  print("__________________________________________")


def display_rules():
  print("Rules:")
  print("- Rock crushes the Scissors")
  print("- Scissor custs the Paper")
  print("- Paper covers the Rock")
  print("- Win the Two games in 3 rounds to become a Champion!")
  print("__________________________________________")

def get_computer_choice():
  return random.randint(1,3)

def get_user_choice():
  print("1. Rock\n2. Paper\n3. Scissors")
  try:
    return int(input("Enter your choice [1-3]:  "))
  except ValueError:
    return 0

def determine_win(user_choice, computer_choice):
  if ((user_choice == 1 and computer_choice == 3) or
      (user_choice == 3 and computer_choice == 2) or
      (user_choice == 2 and computer_choice == 1)):
    return 'user'
  else:
    return 'computer'

def play_game():
  computer_score = 0
  user_score = 0
  total_round = 1

  no_champion = (user_score < 2) or (computer_score < 2) or ((user_score + computer_score) < 3)

  while no_champion:
    print(f"======== ROUND - {total_round} =======")
    print(f"Scores: You: {user_score} - {computer_score} Computer")

    computer_choice = get_computer_choice()
    user_choice = get_user_choice()

    # if user not choose between 1 to 3
    if not user_choice or user_choice > 3:
      print("\nError: Choose number between 1-3 only!\n")
      time.sleep(0.8)
      continue
      
    # if both choose same choice like 1 - 1 or 2 -2  or 3 - 3
    if user_choice == computer_choice:
      print("\nOopss, it's Tie! Please try again...\n")
      time.sleep(0.8)
      continue

    result = determine_win(user_choice, computer_choice)
    if result == 'user':
      print("You win the round!")
      user_score += 1
    else:
      print("Oops, you loose this round")
      computer_score +=1
    
    total_round += 1

    if (user_score == 2):
      print("\nHurry! You win the game!")
      break

    if computer_score == 2:
      print("Sorry, You loose the game")
      break


play_game()