# Wordle CLI

A terminal implementation of Wordle, written in Python with no external dependencies.

Guess a secret 5-letter word within 6 attempts. After each guess, every letter is color-coded to show how close you are.

```
Enter your word: chase
c h a s e
```

- Green: letter is correct and in the right position
- Yellow: letter is in the word but in the wrong position
- Gray: letter is not in the word

## Requirements

- Python 3.8+
- A terminal that supports ANSI escape codes (default on Linux, macOS, and Windows Terminal)

## Installation

```bash
git clone https://github.com/joaorodrigues0764/wordle-cli-py.git
cd wordle-cli-py
```

## Usage

```bash
python3 main.py
```

## How it works

- `load_words()` reads the word list from `words.txt` into memory.
- `get_secret_word()` picks a random word from that list to be the answer.
- `get_user_guess()` prompts for input and validates that it's a 5-letter word from the list.
- `evaluate_guess()` compares the guess against the secret word and prints the color-coded result.
- `main()` runs the game loop, tracking attempts and checking for a win or loss.

## Project structure

```
wordle-cli-py/
├── main.py
├── words.txt
└── README.md
```

`words.txt` contains 2,314 valid 5-letter words, used both as the pool of possible secret words and to validate guesses.

## Contributing

Issues and pull requests are welcome. Some ideas for future work: hint system, guess statistics, word lists for other languages, difficulty levels.

## License

MIT
