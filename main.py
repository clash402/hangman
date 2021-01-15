import random
from hangman_art import stages, logo
from hangman_words import word_list


# METHODS
def lives_are_gone():
    if lives <= 0:
        print("You lose. Try again.")
        return True


def blanks_are_gone():
    if "_" not in display:
        print(stages[lives])
        print(f"{' '.join(display)}")
        print("You win!")
        return True


# MAIN
print(logo)

game_is_in_progress = True

while game_is_in_progress:
    lives = 6
    display = []
    chosen_word = random.choice(word_list)

    # print(f'Hint: the solution is {chosen_word}.')

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

        if lives_are_gone():
            round_is_in_progress = False

        if blanks_are_gone():
            round_is_in_progress = False

    if input("Play another round? (y/n) ").lower() != "y":
        print("Goodbye")
        game_is_in_progress = False
