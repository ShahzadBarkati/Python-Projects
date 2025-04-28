print("Welcome to the Step Counter App!")
print("__________________________________")

daily_goal = int(input("Set your daily step goal: "))
print("__________________________________")
print("Your daily step goal is set to", daily_goal, "steps.")
print("__________________________________")

steps = int(input("Enter the number of steps you took today: "))

if steps <= 0: 
  print("Standup and walk around!")
elif steps < daily_goal:
  print("You are", daily_goal - steps, "steps away from your goal. Keep walking!")
elif steps >= daily_goal:
  print("Congratulations! You have reached your daily goal.")
else: 
  print("Invalid input. Please enter a positive number of steps.")
print("__________________________________")
print("Thank you for using the Step Counter App!")