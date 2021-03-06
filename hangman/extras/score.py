from operator import itemgetter
import csv

class Score:
    def __init__(self, filepath):
        """
            Constructor of Score class object with argument which is path to words scoreboards file.

            Args:
                filepath: Enter path of file, where are scores saved
        """
        self.filepath = filepath


    def make_score_record(self, nickname, letters, attempts, length=0):
        """
            Method for calculating score and returning score record as a list.

            Args:
                nickname: Nickname of player.
                letters: Length of guessed word.
                attempts: Number of lives during a game.
                length: time spend in game.
        """
        totalScore = 100*int(letters)+100*int(attempts)
        return [nickname, totalScore, letters, attempts, length]
        

    def save_score(self, scorerecord):
        """
            Method for saving score record to scoreboards file.

            Args:
                scorerecord: Score record which is going to be saved in scoreboards. For better funcionality of game it SHOULD be a list.
        """
        with open(self.filepath, "a") as file:
            writer = csv.writer(file, delimiter=",")
            writer.writerow(scorerecord)

    
    def load_score_data(self):
        """
            Method for loading data. CAUTION! Method is loading only nickname of player and his score.
        """
        scoreBoardsLocal = []
        with open (self.filepath, "r") as file:
            for line in csv.reader(file, delimiter=","):
                line = [line[0], int(line[1])]
                scoreBoardsLocal.append(line)
        return scoreBoardsLocal


    def print_score(self, scoreboards):
        """
            Method for printing scoreboards ingame in format Nick : Score.

            Args:
                scoreboards: Input data which are going to be printed.
        """
        temp = 0
        for nickname, score in scoreboards:
            nickLenght = 10 - len(nickname)
            print(" " * nickLenght + f"{nickname} : {score}")
            temp += 1
            if temp == 10:
                break
            
            
    def sort_score(self, scoreboards):
        topTen = sorted(scoreboards, key=lambda x: x[1], reverse=True)
        return topTen
