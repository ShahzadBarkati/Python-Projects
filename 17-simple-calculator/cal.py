def add(a, b):
  return a + b

def sub(a, b):
  return a - b

def mult(a, b):
  return a * b

def divide(a, b):
  if b == 0:
    return "Error: Division by Zero is not allowed!!"
  return a / b

def main():
  print("Welcome to the Simple Calculator")
  print("_______________________________________")

  print("\n1. Addition(+)\n2. Substraction(-) \n3. Multiplication(*)\n4. Division(/) ")

  while True:
    choice = input("\nChoose your operation: [1 - 4]: ")

    if choice not in ["1", "2", "3", "4"]:
      print("\nPlease choose valid number between 1 to 4.")
      continue
    else: 
      break

  try: 
    num1 = float(input("\nEnter first number: "))
    num2 = float(input("Enter second number: "))
  except ValueError:
    print("Error: Only numbers allowed for calculation.")
    return 
  
  if choice == "1": 
    print(f"{num1} + {num2} = {add(num1, num2)}")
  elif choice == "2":
    print(f"{num1} - {num2} = {sub(num1, num2)}")
  elif choice == "3":
    print(f"{num1} * {num2} = {mult(num1, num2)}")
  else:
    print(f"{num1} / {num2} = {divide(num1, num2)}")

  if not input("\nDo you want to again perform calculation (Y/N)? ").lower().startswith('y'):
    print("\nGood bye...")
    return 
  else: 
    main()


main()