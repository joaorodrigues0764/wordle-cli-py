import random

def main():
    """
    Runs the game loop: pick a secret word, then give the player
    six attempts to guess it.
    """
    words_list = load_words()
    secret_word = get_secret_word(words_list)

    attemps = 1

    while attemps <= 6:
        user_guess = get_user_guess(words_list)
        evaluate_guess(secret_word, user_guess)

        if secret_word == user_guess:
            print("Congratulations, You Won!!!")
            break

        attemps += 1

    if attemps > 6 :
        print("You lost :( The word was", secret_word, "!")

def load_words():
    """
    Reads words.txt line by line and returns them as a list.
    strip() is used to remove the trailing newline from each line.
    """
    words_list = []

    with open("words.txt", "r") as file:
        for line in file:
            words_list.append(line.strip())

    return words_list

def get_secret_word(words_list):
    """
    Picks a random word from the list to be the answer for this round.
    """
    secret_word = random.choice(words_list)

    return secret_word

def get_user_guess(words_list):
    """
    Keeps asking the player for a guess until it's a valid one:
    exactly 5 letters and present in the word list. strip() removes
    extra whitespace and lower() normalizes the casing.
    """
    while True:
        user_guess = input("Enter your word: ").strip().lower()
        if len(user_guess) != 5:
            print("The word must have 5 letters!")
        elif user_guess not in words_list:
            print("The word is not in the word list, try again!")
        else:    
            return user_guess
                                                                                                    
def evaluate_guess(secret_word, user_guess):
    """
    Compares the guess against the secret word letter by letter and
    prints it back with color highlighting: green for a correct
    letter in the correct spot, yellow for a correct letter in the
    wrong spot, and gray for a letter that isn't in the word at all.
    """
    secret_word_list = list(secret_word)
    user_guess_list = list(user_guess)

    result = ["", "", "", "", ""]

    GREEN = "\033[42m\033[30m"
    YELLOW = "\033[43m\033[30m"    
    GRAY = "\033[100m\033[97m"
    RESET = "\033[0m"

    # First pass: mark exact matches (green) and remove them from
    # secret_word_list so they don't get reused as yellow matches later.
    i = 0
    while i < 5:
        if secret_word_list[i] == user_guess_list[i]:
            result[i] = f"{GREEN}{user_guess_list[i]}{RESET}"
            secret_word_list[i] = '_'
        i += 1

    # Second pass: for the letters that weren't exact matches, check
    # if they still appear somewhere else in the secret word (yellow),
    # otherwise mark them as not present (gray).
    i = 0
    while i < 5:
        if result[i] == "":
            if user_guess_list[i] in secret_word_list:
                result[i] = f"{YELLOW}{user_guess_list[i]}{RESET}"
                secret_word_list.remove(user_guess_list[i]) 
            else:
                result[i] = f"{GRAY}{user_guess_list[i]}{RESET}"
        i += 1

    print("".join(result))

if __name__ == "__main__":
    main()