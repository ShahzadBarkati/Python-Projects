print("Welcome to the Text Formatter!")
print("_________________________________________________")

text = input("Please enter the text you want to format: ")
print("_________________________________________________")
print("Choose the formatting option you want to apply:")
print("1. Uppercase") 
print("2. Lowercase")
print("3. Title Case")
print("4. Sentence Case / Capitalize")
print("5. Reverse")
print("6. Remove Extra Spaces")

option = int(input("Enter the number of your choice: "))
print("_________________________________________________")

print("Formatted Text:")

if option == 1:
  print(text.upper())
elif option == 2:
  print(text.lower())
elif option == 3:
  print(text.title())
elif option == 4:
  print(text.capitalize())
elif option == 5:
  print(text[::-1])
elif option == 6:
  print(" ".join(text.split()))
else:
  print("Invalid option. Please try again.")
print("_________________________________________________")
print("Thank you for using the Text Formatter!")
print("_________________________________________________")