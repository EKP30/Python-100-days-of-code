#Number Guessing Game Objectives:
# Include an ASCII art logo.
def game():
  from random import randint
  logo = """
    _____                   ________         _  __           __          
   / ___/_ _____ ___ ___   /_  __/ /  ___   / |/ /_ ____ _  / /  ___ ____
  / (_ / // / -_|_-<(_-<    / / / _ \/ -_) /    / // /  ' \/ _ \/ -_) __/
  \___/\_,_/\__/___/___/   /_/ /_//_/\__/ /_/|_/\_,_/_/_/_/_.__/\__/_/ 
  """
  EASY_DIFFICULTY_TURNS = 10
  HARD_DIFFICULTY_TURNS = 5
  game_over = False
  random_number = randint(1, 100)
  print(logo)
  print("Welcome to the number guessing game!\nI am thinking of a number between 1 and 100.")
  difficulty_choice = input("Choose a difficulty. Type 'easy' or 'hard': ")
  while game_over == False:
    if difficulty_choice == "easy":
      easy_number_guess = input(f"You have {EASY_DIFFICULTY_TURNS} attempts left to guess the number.\nMake a guess: ")
      easy_number_guess = int(easy_number_guess)
      EASY_DIFFICULTY_TURNS -= 1
      if easy_number_guess == random_number:
        print(f"You got it! The answer was {random_number}.")
        game_over = True
      elif easy_number_guess > random_number:
        print("Too high.")
      elif easy_number_guess < random_number:
        print("Too low.")
    elif difficulty_choice == "hard":
      hard_number_guess = input(f"You have {HARD_DIFFICULTY_TURNS} attempts left to guess the number.\nMake a guess: ")
      hard_number_guess = int(hard_number_guess)
      HARD_DIFFICULTY_TURNS -= 1
      if hard_number_guess == random_number:
        print(f"You got it! The answer was {random_number}.")
        game_over = True
      elif hard_number_guess > random_number:
        print("Too high.")
      else:
        print("Too low.")
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
def game_without_infinite_turns():
  from random import randint
  logo = """
    _____                   ________         _  __           __          
   / ___/_ _____ ___ ___   /_  __/ /  ___   / |/ /_ ____ _  / /  ___ ____
  / (_ / // / -_|_-<(_-<    / / / _ \/ -_) /    / // /  ' \/ _ \/ -_) __/
  \___/\_,_/\__/___/___/   /_/ /_//_/\__/ /_/|_/\_,_/_/_/_/_.__/\__/_/ 
  """
  EASY_DIFFICULTY_TURNS = 10
  HARD_DIFFICULTY_TURNS = 5
  game_over = False
  random_number = randint(1, 100)
  print(logo)
  print("Welcome to the number guessing game!\nI am thinking of a number between 1 and 100.")
  difficulty_choice = input("Choose a difficulty. Type 'easy' or 'hard': ")
  while game_over == False:
    if difficulty_choice == "easy":
      easy_number_guess = input(f"You have {EASY_DIFFICULTY_TURNS} attempts left to guess the number.\nMake a guess: ")
      easy_number_guess = int(easy_number_guess)
      EASY_DIFFICULTY_TURNS -= 1
      if easy_number_guess == random_number:
        print(f"You got it! The answer was {random_number}.")
        game_over = True
      elif easy_number_guess > random_number:
        print("Too high.")
        if EASY_DIFFICULTY_TURNS == 0:
          game_over = True
      elif easy_number_guess < random_number:
        print("Too low.")
        if EASY_DIFFICULTY_TURNS == 0:
          game_over = True
    elif difficulty_choice == "hard":
      hard_number_guess = input(f"You have {HARD_DIFFICULTY_TURNS} attempts left to guess the number.\nMake a guess: ")
      hard_number_guess = int(hard_number_guess)
      HARD_DIFFICULTY_TURNS -= 1
      if hard_number_guess == random_number:
        print(f"You got it! The answer was {random_number}.")
        game_over = True
      elif hard_number_guess > random_number:
        print("Too high.")
        if HARD_DIFFICULTY_TURNS == 0:
          game_over = True
      else:
        print("Too low.")
        if HARD_DIFFICULTY_TURNS == 0:
          game_over = True



game_without_infinite_turns()