print("Welcome to Char type Checker!")
print("_____________________________________________")

c = input("Enter a single character: ")

if c.isdigit():
  print(f"{c} is a digit.")
elif c.isalpha():
  print(f"{c} is an alphabet.")
elif (not c.isdigit()) and (not c.isspace() and not c.isalpha()):
  print(f"{c} is a special character.")
else:
  print(" You entered a whitespace.")
print("_____________________________________________")
print("Thank you for using Char type Checker!")
print("_____________________________________________")
