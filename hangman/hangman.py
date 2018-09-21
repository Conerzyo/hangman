from extras.words import Words
from extras.score import Score
from extras.game import Game
from os import system
from time import sleep


def play_again():
    # Fuction for cleaner code. Asking player if he wants to play again.
    again = str.upper(input("\nDo you want to play again? Y/N:"))
    if again == "Y":
        system("clear")
        willToPlay = True
    elif again == "N":
        willToPlay = False
        exit()
    else:
        print("WRONG INPUT AND IT CRASHED!")
        exit()
    return willToPlay


def write_menu():
    system("clear")
    print("Welcome to Hangman game")
    print("-"*23)
    print("MAIN MENU")
    print("1: New game")
    print("2: Scoreboards")
    print("3: Add word to library")
    print("4: Exit")
    print("-"*23)


def write_score(game):
    system("clear")
    print("S C O R E B O A R D S")
    print("-"*21)
    game.print_score()
    print("-"*21)
    input("Push any key for going back to menu...")
    system("clear")


def write_nick(game):
    nickname = str.capitalize(input("\nGood, you were right. YOU WIN! Write down your nickname: "))
    while len(nickname) > 6:
        system("clear")
        print("WRONG INPUT!")
        nickname = str.capitalize(input("\nWARNING! Nick has to be max 6 characters long. \n\nWrite down your nickname again: "))
    if nickname != "":
        game.save_score(nickname, game.attempts, 0)
        play_again()
    else:
        play_again()


def write_word(game):
    system("clear")
    game.add_word(str.lower(input("Enter a word you want to add to the library of words: ")))
    sleep(1)
    system("clear")


def play_game(game):
    system("clear")
    print("Here is your word. LETS GUESS!")
    print(" "*10 + "Good luck!\n")
    print("-"*30)
    print()
    game.new_game(5)
    print(game.get_guessed_word())
    while game.is_game_running():
        tip = str.lower(input("Guess a letter: "))
        print()
        game.guess_letter(tip)
        print(game.get_guessed_word())
    if game.is_game_won():
        write_nick(game)
    else:
        print("\nYou are out of attempts, GAME OVER!.")
        play_again()


words = Words("extras/library.txt")
score = Score("extras/scoreboards.csv")

try:
    words.load_data()
except (IOError, IndexError):
    print("Something somewhere went terribly wrong")
    exit()

game = Game(words, score)

willToPlay = True
while willToPlay == True:
    write_menu()
    userChoice = int(input("What is your choice?: "))
    if userChoice == 1:
        play_game(game)
    elif userChoice == 2:
        write_score(game)
    elif userChoice == 3:
        write_word(game)
    elif userChoice == 4:
        break
    else:
        print("WRONG INPUT...")
        exit()

system("clear")
print("Thanks for playing! Bye, bye.")
