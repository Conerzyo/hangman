from os import system

class Game:
    def __init__(self, words_service, score_service):
        """
        Constructor of Game class object with arguments given via composition. Object will get access to methods of Words and Score classes.
        Also is set game_runnning to False.

        Args:
            word_service: Object of Words class
            score_service: Object of Score class
        """
        self.words_service = words_service
        self.score_service = score_service
        self.game_running = False

    
    def new_game(self, num_attempts):
        """
            Method which creates new game with given number of available attempts. New game pick random word from library automaticaly.

            Args:
                num_attempts: Number of attempts before game ends.
        """
        self.secretWord = self.words_service.pick_word()
        self.attempts = num_attempts
        # Makes list of "_" chars in lenght of secret word
        self.guessedWord = ["_" for x in range(self.get_word_length())]
        # new game implicit settings
        self.game_running = True
        self.game_won = False


    def get_word_length(self):
        """
            Method is returning length of secret word as integer.
        """
        if not self.is_game_running:
            raise RuntimeError("Game is not running")
        return len(self.secretWord)

    
    def get_guessed_word(self):
        """
            Method returning state of guessed word during a game.
        """
        if not self.is_game_running:
            raise RuntimeError("Game is not running")
        return " ".join(self.guessedWord)

    
    def is_game_running(self):
        return self.game_running

    
    def is_game_won(self):
        return self.game_won

    
    def _check_game_won(self):
        """
            Method checks if is "_" char in guessed word and evaluate if game is won or not.
        """
        return "_" not in self.guessedWord

    
    def _check_game_lost(self):
        return self.attempts == 0


    def guess_letter(self, letter):
        """
            Method which is whole core of game. Working with given letter and checking if it is in secret word then saves it to guessed word.import pudb; pudb.set_trace()

            Args:
                letter: Letter entered by player.
        """
        if letter in self.secretWord:
            if letter in self.guessedWord:
                return True

            for index, char in enumerate(self.secretWord):
                if char == letter:
                    self.guessedWord[index] = letter

            if self._check_game_won():
                self.game_won = True
                self.game_running = False
            return True

        else:
            self.attempts -= 1
            if self._check_game_lost():
                self.game_won = False
                self.game_running = False
            return False

    # functional methods for better "security" in game.
    def save_score(self, nickname, attempts, lenght=0):
        score = self.score_service.make_score_record(nickname, self.get_word_length(), attempts, lenght)
        self.score_service.save_score(score)

    
    def print_score(self):
        scoreboards = self.score_service.load_score_data()
        topTen = self.score_service.sort_score(scoreboards)
        self.score_service.print_score(topTen)


    def add_word(self, word):
        self.words_service.add_word(word)