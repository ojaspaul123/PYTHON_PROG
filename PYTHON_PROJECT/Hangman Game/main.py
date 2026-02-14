# Hanging Game
from wordlist import words
import random


hangman_art = {0:(" ",
                  " ",
                  " "),
               1: (" o ",
                   " ",
                   " "),
               2:(" o ",
                  " | ",
                  " "),
               3:(" o ",
                  "/| ",
                  " "),
               4:(" o ",
                  "/|\\",
                  " "),
               5:(" o ",
                  "/|\\ ",
                  "/ "),
               6:(" o ",
                  "/|\\",
                  "/ \\")}

def display_man(wrong_guesses):
    print("--------------------------")
    for line in hangman_art[wrong_guesses]:
        print(line)
    print("--------------------------")
        
def display_hint(hint):
    print(" ".join(hint))
    
def display_answer(answer):
    print(" ".join(answer))    

def main():
    answer = random.choice(list(words))
    hint = ["_"] * len(answer)
    wrong_guesses =0
    guessed_letters = set()
    isrunning = True
    
    while isrunning:
        display_man(wrong_guesses)
        display_hint(hint)
       
        guess = input("Enter a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        
        if guess in guessed_letters:
            print(f"You already guessed that letter.\n : {guess}")
            continue
        
        guessed_letters.add(guess)
        
        if guess in answer:
            for i in range (len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
                    
        else:
            wrong_guesses += 1
        
        if "_" not in hint:
           display_man(wrong_guesses)
           print("You win! The word was:")
           display_answer(answer)
           isrunning = False
    

        elif wrong_guesses >= len(hangman_art) - 1:
            display_man(wrong_guesses)
            print("You Lose! The word was:")
            display_answer(answer)
            isrunning = False           
        
if __name__ == "__main__":
    main()