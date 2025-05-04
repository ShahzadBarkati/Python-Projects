import time

print("Welcome to the Countdown Timer")
print("_______________________________________")

loop = True
countdown = 1


while True:
  try:
    if loop:
      choice = int(input("Enter the maximum second to countdown from: "))

    loop = False

    if countdown > choice: 
      print(f"\nCountdown is COMPLETED!!")
      break
      
    print(f"{(choice + 1) - countdown} seconds remaining...")
    time.sleep(1)
    countdown += 1

  except ValueError:
    print(f"\nPlease enter the valid second between 1 to 60!")
    loop = True
    continue