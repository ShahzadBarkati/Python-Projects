print("Welcome to the Vowel Counter App")
print("_______________________________________________")

# Simple syntax

# while True:
#   text = input("\nEnter some text ( or 'exit' to quit): ")

#   if text.lower() == 'exit':
#     print("Good Byeee...")
#     break

#   vowels = 0

#   for l in text:
#     if l.lower() in ["a", "e", "i", "o", "u"]:
#       vowels += 1; 

#   print(f"Total vowel counts in {text} is: {vowels}")
#   print("_______________________________________________")

    
# Advance Syntax

while True:
  text = input("\nEnter some text ( or 'exit' to quit): ")

  if text.lower() == 'exit':
    print("Good Byeee...")
    break

  vowels = sum(1 for c in text if c.lower() in 'aieou')   #  <------

  print(f"Total vowel counts in {text} is: {vowels}")
  print("_______________________________________________")
