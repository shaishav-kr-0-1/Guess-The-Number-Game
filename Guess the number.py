import random

def guess_the_number():
  print("Welcome to Guess the Number game!")
  play_game = input("Do you want to play? (yes/no): \n")
  if play_game.lower() != "yes":
    print("Thanks for coming!")
    return
  print("\nLet's begin!")
  secret_number = random.randint(1, 50)
  print("I have chosen a secret number between 1 and 50.")
  print("You need to guess the number.")
  difficulty_level = input("Choose a difficulty level (easy/hard): \n")
  if difficulty_level.lower() == "easy":
    max_attempts = 6
  elif difficulty_level.lower() == "hard":
    max_attempts = 3
  else:
    print("Invalid input .", )
    exit()
  print("\nYou have", max_attempts, "attempts to guess the number.")
  for attempt in range(1, max_attempts + 1):
    guess = int(input("Attempt {}: Guess the number: ".format(attempt)))

    if guess == secret_number:
      print("\nCongratulations! You won!")
      return
    elif guess < secret_number:
      print("Your guess is too low.")
    else:
      print("Your guess is too high.")
  print("\nSorry, you ran out of attempts. The secret number was",
        secret_number)


guess_the_number()
