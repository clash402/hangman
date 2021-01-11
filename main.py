import random
from hangman_art import stages, logo
from hangman_words import word_list


# MAIN
print(logo)

game_is_in_progress = True

while game_is_in_progress:
  lives = 6
  display = []
  chosen_word = random.choice(word_list)

  # print(f'Pssst, the solution is {chosen_word}.')

  for _ in chosen_word:
    display.append("_")

  round_is_in_progress = True

  while round_is_in_progress:
    print(stages[lives])
    print(f"{' '.join(display)}")
    guess = input("Guess a letter: ").lower()

    # clear()

    if guess in display:
      print(f"You've already guessed {guess}. Try a new letter.")
      continue

    for i, letter in enumerate(chosen_word):
      if letter == guess:
        display[i] = letter

    if guess not in chosen_word:
      lives -= 1
      print(f"You guessed {guess}. That letter isn't in the word.")

    if lives <= 0:
      round_is_in_progress = False
      print("You lose. Try again.")

    if "_" not in display:
      round_is_in_progress = False
      print(stages[lives])
      print(f"{' '.join(display)}")
      print("You win!")

  user_answer = input("Play another round? (y/n) ").lower()

  if user_answer != "y":
    print("Goodbye")
    game_is_in_progress = False
