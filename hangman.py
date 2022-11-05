"""
The program will depict a game of hangman.
Name: Sufyan Chaudhry
"""

import random 
name = input("Hi, what's your name? ")  
print("Ok,", name, "You get 12 chances and you can guess up to 12 different words.")
print("Lets Play!")


bank = ["yellow", "couch", "german", "chocolate", "pakistan", "crocodile", "pirate", "would", "python", "college", "wedding", "basketball"]
repeat = "y"

while repeat == "y":
    
    lettersGuessed = ""
    lives = 12
    word = random.choice(bank)
    done = False
    
    while not done and lives !=0:
        g = input("\nWhat is your guess: ")
        
        if g in word:
            print("correct")
        else:
            print("no, sorry try again!")
            lives = lives -1
            print("\nYou have", lives,"lives left.")
        lettersGuessed = lettersGuessed + g
        wrong = 0
        for letters in word:
            if letters in lettersGuessed:
                print(letters, end=" ")
            else:
                print("_", end=" ")
                wrong = wrong + 1
        done = True

        for letter in word:
            if letter not in lettersGuessed:
                done = False
        if wrong == 0:
            print("\nYou won!!")
            repeat = "n"
            break

        if lives ==0:
            print("\nGame Over!! You lost! :(. The word was", word)
            

    repeat = input("\nWould you like to play again (y/n): ")
print("Thanks for playing!!!")
