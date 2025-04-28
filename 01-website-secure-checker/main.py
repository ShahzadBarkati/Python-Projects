print("Welcome to the Website Secure Checker!")
print("-----------------------------------------------")
site = input("Enter the website URL: ")
if site.startswith("https://"):
  print("The website is secure.")
elif site.startswith("http://"):
  print("The website is not secure.")
else:
  print("Invalid URL. Please enter a valid website URL starting with 'http://' or 'https://'.")

print("Thank you!!!")

