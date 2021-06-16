# Imports... Boring stuff. 
import random
# Gets a "Random" number.
rn = random.randint(1,100)
print("Welcome to Sky's random number guesser game!")
# Difficulty Stuff
print("Difficulties are Easy, Normal, Hard.")
difficulty = input("Select a difficulty: ").lower()

# Vars.. 
difficulties = {
  "easy": 10,
  "normal": 7,
  "hard": 3
}
tries = difficulties.get(difficulty)
# Welcome Message
print("Guess the random number between 1 and 100!")

# The game loop.
while tries > 0:
    print(f"You have {tries} tries left!")
    guess = input("Guess the number?: ")
    # Makes sure ppl dont strings in my input field! 
    try: 
        guess_int = int(guess)
        if guess_int < rn:
            print("Higher!")
            tries -= 1
        elif guess_int > rn:
            print("Lower!")
            tries -= 1
        elif guess_int == rn:
            print("You win!")
            break
    # Raises an error instead of crashing the app.
    except ValueError: 
        print("This is not a number!")
if tries == 0:
    print("Game Over! Restart the program to try again!")
    print(f"P.S. Your number was {rn}")
else:
    tries_taken = tries - difficulties.get(difficulty)
    tries_taken = -tries_taken
    tries_taken = tries_taken + 1
    print(f"You win! It took {tries_taken} Tries!")