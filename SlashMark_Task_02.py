#!/usr/bin/env python
# coding: utf-8

# In[7]:


import random
import time

def intro():
  """
  Greets the player with a random encouraging phrase and offers a short tutorial.
  """
  name = input("May I ask for your name? ")  # Ask for the name
  greetings = [
      f"🎉 Welcome, {name}! Let's play a guessing game. I'm thinking of a number...",
      f"🤔 Ready to test your intuition, {name}? I've chosen a number (1-200). Can you guess it? ",
      f"🎲 Up for a challenge, {name}? Guess the number I'm thinking of!",
  ]
  print(random.choice(greetings))
  print(
      "This game has difficulty levels. Higher difficulty gives you fewer guesses. \n"
      "I'll provide hints based on how close your guess is to the actual number. \n"
      "Good luck! 🍀"
  )
  return name

# ... (rest of the code remains unchanged)


def pick(name):
  """
  Handles the guessing logic with difficulty levels, hints based on closeness, 
  and keeps track of remaining guesses.

  Args:
      name: Player's name.
  """
  guesses_taken = 0
  difficulty = choose_difficulty()
  number = random.randint(1, 200)
  remaining_guesses = difficulty

  while remaining_guesses > 0:
    time.sleep(0.25)
    enter = input("Guess: ")
    try:
      guess = int(enter)

      if 1 <= guess <= 200:
        guesses_taken += 1
        remaining_guesses -= 1
        if guess == number:
          break
        elif guess < number:
          hint = "That's a bit low. Try a higher number ⬆️"
          if remaining_guesses <= 2:
            hint += " You only have a few guesses left! ⌛"
        else:
          hint = "That's a bit high. Try a lower number ⬇️"
          if remaining_guesses <= 2:
            hint += " You only have a few guesses left! ⌛"
        print(hint)
      else:
        print("🙈 Silly Goose! That number isn't in the range (1-200). ")

    except ValueError:
      print(f"I don't think '{enter}' is a number. Please try again.")

  if guess == number:
    guesses_taken_str = str(guesses_taken)
    print(
        f'🎉 Good job, {name}! You guessed my number in {guesses_taken_str} guesses!'
    )
    score = calculate_score(difficulty, guesses_taken)
    print(f"Your score: {score} 🏆")
  else:
    print(f'Nope. The number I was thinking of was {number}.')

def choose_difficulty():
  """
  Prompts the player to choose a difficulty level with a short description.

  Returns:
      int: The number of guesses allowed based on difficulty.
  """
  print("\nChoose difficulty:")
  print("1. Easy (8 guesses) - Take it slow and steady.")
  print("2. Normal (6 guesses) - The sweet spot for a challenge.")
  print("3. Hard (4 guesses) - Are you feeling lucky? ")
  while True:
    choice = input("Enter your choice (1-3): ")
    try:
      difficulty = int(choice)
      if 1 <= difficulty <= 3:
        return {1: 8, 2: 6, 3: 4}[difficulty]
      else:
        print("Invalid choice. Please enter a number between 1 and 3.")
    except ValueError:
      print("Invalid choice. Please enter a number.")

def calculate_score(difficulty, guesses_taken):
  """
  Calculates the player's score based on difficulty and number of guesses.

  Args:
      difficulty: The chosen difficulty level.
      guesses_taken: The number of guesses it took to guess the number.

  Returns:
      int: The player's score.
  """
  max_score = 100
  penalty_factor = 10
  score = max(0, max_score - penalty_factor * (difficulty - guesses_taken))
  return score

play_again = "yes"
while play_again.lower() in ("yes", "y"):
  name = intro()
  pick(name)
  print("\nDo you want to play again? 🔄")
  play_again = input()

print("Thanks for playing! See you next time. 👋")


# In[ ]:




