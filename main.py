import random
from difficulty import Difficulty

def load_words(difficulty_level):
    """Loads random words from a dictionary with length equal to difficulty"""
    dictionary = open("popular.txt").readlines()
    words = []
    while len(words) < 10:
        word = random.choice(dictionary)
        word = word.rstrip('\r\n')
        if len(word) == difficulty_level:
            if word not in words:
                words.append(word)
    return words

def count_positions(guess, password):
    """Counts how many letter positions are correct for a guess"""
    count = 0
    for a, b in zip(guess, password):
        if a == b:
            count = count + 1
    return count

def select_difficulty(user_difficulty):
    """Get the difficulty enum from user input"""
    try:
        return Difficulty[user_difficulty.upper()].value
    except KeyError:
        print("Unknown command")

def start_game():
    """Start the game and get the difficulty, word list and password"""
    print("Select difficulty: (novice, advanced, expert, master)")
    user_difficulty = input()
    difficulty = select_difficulty(user_difficulty)
    word_list = load_words(difficulty)
    password = random.choice(word_list)
    game_loop(word_list, password)

def game_loop(words, password):
    """Main game loop which interacts with the user"""
    attempts = 4
    for word in words:
            print(word.upper())
    while attempts > 0:
        print("Guess? (", attempts, " left) ")
        guess = input()
        if guess in words:
            attempts = attempts - 1
            likeness = count_positions(guess, password)
            if guess == password:
                print("Success! You hacked the terminal")
                return
            else:
                print("Entry denied.")
                print("Likeness=", likeness)
        else:
            print("Unknown command")
    print("You failed! The password was", password)
start_game()
