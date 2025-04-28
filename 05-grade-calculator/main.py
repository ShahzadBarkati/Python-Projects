print("Welcome to the Grade Calculator!")
print("______________________________________________")
print("NOTE: Score: 90 >= A, 80 >= B, 60 >= C, 35 >= D,  35 < F")
print("______________________________________________")

scores = []

while True: 
  score = input("Enter test score ( or 'done' ): ")
  if score.lower() == "done":
    break

  try:
    score = int(score)
    scores.append(float(score))
  
  except ValueError:
    print("Please enter a valid number.")
    continue


avg = sum(scores) / len(scores)
print(f"Your average is: {avg:.1f}")

if avg >= 90:
  print("You got an A Grade!")
elif avg >= 80:
  print("You got a B Grade!")
elif avg >= 60:
  print("You got a C Grade!")
elif avg >= 35:
  print("You got a D Grade!")
else:
  print("You Failed!")    

print("Goodbye!")

