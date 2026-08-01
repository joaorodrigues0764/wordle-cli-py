import random

def main():
    """
    This is the main function. The heart of the game is in here!
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
    This function copys the words in the .txt file to a new list named as "words_list".
    .strip() cuts of the '\n'
    """
    words_list = []

    with open("words.txt", "r") as file:
        for line in file:
            words_list.append(line.strip())

    return words_list

def get_secret_word(words_list):
    """
    This function uses "random" to choose a random word from the list.
    That random word will be our secret word.
    """
    secret_word = random.choice(words_list)

    return secret_word

def get_user_guess(words_list):
    """
    This function asks the player for his guess and makes sure that the guess is valid.
    The .strip() eliminates the spaces and the .lower() converts every letters into lowercase.
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
    This function compares each letter of the secret_word and user_guess and determines
    wether it must be paint in green, yellow or gray.
    When it finishes, it displays the result so the player can see how he did.
    """
    secret_word_list = list(secret_word)
    user_guess_list = list(user_guess)

    result = ["", "", "", "", ""]

    GREEN = "\033[42m\033[30m"
    YELLOW = "\033[43m\033[30m"    
    GRAY = "\033[100m\033[97m"
    RESET = "\033[0m"

    i = 0
    while i < 5:
        if secret_word_list[i] == user_guess_list[i]:
            result[i] = f"{GREEN}{user_guess_list[i]}{RESET}"
            secret_word_list[i] = '_'
        i += 1

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