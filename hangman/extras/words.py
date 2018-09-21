from random import randrange
import re

class InvalidWordFormat(Exception):
    pass


class Words:
    def __init__(self, filepath):
        """
            Constructor of Words class object with argument which is path to words library file.

            Args:
                filepath: Enter path of file, where are words saved
        """
        self.filepath = filepath
        self.wordlist = []


    def load_data(self):
        """
            Method for loading data (words) from library and saving them as a list.
        """
        self.clear_data()
        with open(self.filepath, "r") as file:
            for line in file.readlines():
                word = line[:-1]
                self.wordlist.append(word)


    def add_word(self, word):
        """
            Method for adding word to library file. Using regular expression for check validity of entered word.

            Args:
                word: Word which is going to be saved to library
        """
        if self.check_word(word):
            raise InvalidWordFormat(f"You screwed up! '{word}' cannot be added!")
        self.wordlist.append(word)
        with open(self.filepath, "a") as file:
            file.write(word + "\n")
            print("Word has been added to library!")


    #metoda slouzici pro zkontrolovani slova vrati false kdyz je slovo v poradku a true kdyz neni
    def check_word(self, word):
        """
            Method for checking word validity. Returning False if you do not need to check word and True if you have to.

            Args:
                word: Word which is going to be checked via regular expression
        """
        if not re.match("(^[a-zA-Z]+$)", word):
            return True
        return False


    #vyber z nasi vnitrni databaze nahodne slovo, v podstate stejne jako to tvoje
    def pick_word(self):
        """
            Method for selecting random word from list loaded from library file.
        """
        random_index = randrange(len(self.wordlist))
        randomWord = self.wordlist[random_index]
        return str(randomWord)

    #metoda na vyresetovani dat - jasnej nazev tak vis kdekoli je v kodu co dela
    def clear_data(self):
        self.wordlist = []