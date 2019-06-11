import string
import random

user_length = int(input("How many letters does your word have? "))
word_guess = ["_"] * user_length

# Current spaces in word
def current_word_letters():
    for i in word_guess:
        print(i + " ", end="")

print("\n")

current_word_letters()

print("\n")
guess_counter = 0
guess_list = []

while "_" in word_guess:
    guess_letter = random.choice(string.ascii_lowercase) # Random letter generator for guesses  
    if guess_letter not in guess_list:
        guess_list.append(guess_letter)
        this_guess = guess_letter # Ready for non-repeating list
        user_conf = input(f"\nDoes your word contain the letter {this_guess.upper()}\n\nHit Y for Yes or N for No: ").upper()
        if user_conf == "Y":
            letter_position = input(f"\nWhat number letter is {this_guess.upper()} in your word?: ")
            letter_position = letter_position.split(",")
            for x in letter_position:
                x = int(x) - 1
                word_guess.pop(int(x))
                word_guess.insert(int(x),f"{this_guess}")
            for i in word_guess:
                print(i + " ", end="")
        else:
            guess_counter = guess_counter + 1 
    if guess_counter == 10:
        print("\nLooks like I'm out of guesses - you win!")
        break      
    elif "_" not in word_guess:
        s = ""
        s = s.join(word_guess)
        print(f"\nYay! I won! Your word is {s.upper()}")