print("Welcome to the Reverse Name App")
print("_______________________________________________")

while True:
  name = input("Enter a name: ")
  reverse_name = name[::-1]
  print(f"Reverse Name: '{reverse_name}'1")
  print(f"In parallel universe they call you '{reverse_name.title()}'")

  answer = input("Try another name? (Y/N) ")
  if answer.lower() == 'n':
    print("Thank you!!")
    break
  else:
    continue