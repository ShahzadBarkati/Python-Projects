import random


print("Welcome to the Music Recommender!")
print("_____________________________________")

genres = {
  'rock': ['Queen', 'AC/DC', 'Led Zeppelin' ],
  'pop': ['Tailor Swift', 'Ed Sheeran', 'Ariana Grande'],
  'hip-hop': ['Kendrick Lamar', 'Drake', 'J. Cole']
}

while True: 
  choice = input("Which genre do you like: [Rock, Pop, Hip-hop]? (or 'exit to quit):  ").lower()

  if choice.lower() == 'exit':
    print("Good Byeee...")
    break

  if choice.lower() not in genres: 
    print("Sorry you choose wrong option! try again...")
    continue
  else:
    print(f"Check out: ' { random.choice(genres[choice.lower()])} '")
  
print("Thank you!")