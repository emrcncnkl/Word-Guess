import random

words = ["apple", "computer", "book", "chair", "table", "glasses", "phone", "pen", "notebook", "watch", "shoe", "bag", "hat", "jacket", "pants", "shirt", "sweater", "lighting", "television", "radio", "microphone", "speaker", "headphones", "keyboard", "mouse", "printer", "scanner", "camera", "camera", "washing machine", "refrigerator", "oven", "microwave", "dishwasher", "hood", "blender", "toaster", "kettle", "hairdryer", "razor", "toothbrush", "comb", "mirror", "umbrella", "socks", "shoe", "boot", "sandal", "slipper", "sneaker", "wallet", "key", "cell phone", "tablet"]

continue_game = 'y'
while continue_game == 'y':
    selected_word = random.choice(words)
    guesses = []
    wrong_guesses_count = 0
    limit = 5

    while wrong_guesses_count < limit:
        guess = input("Enter the letter you guess: ")
        guess = guess.lower()

        if guess in selected_word:
            print("Correct Guess!")
            guesses.append(guess)
        else:
            print("Wrong Guess...")
            wrong_guesses_count += 1

        for letter in selected_word:
            if letter not in guesses:
                print("The game continues.")
                break
        else:
            print("Correct Guess! You've Guessed it.")
            break

    if wrong_guesses_count >= limit:
        print("Sorry, you lost the game.")

    continue_game = input("Do you want to play another game? (y/n)")
    continue_game = continue_game.lower()
