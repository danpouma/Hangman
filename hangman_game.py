from Tkinter import *

class Hangman():
    def __init__(self):
        self.word = Word()
        self.player = Player()
        self.gui = HangmanGUI()
        self.create_gui()
        
    def create_gui(self):
        self.gui.create_button()
        self.gui.create_frames()
        self.gui.display_word("")
        self.gui.display_wrong_letters("")
        self.gui.display_character()
        #self.gui.mainloop()

    def get_word(self):
        return self.word.get_word()

    def get_guesses(self):
        return self.player.get_guesses()

    def increment_guesses(self):
        return self.player.increment_guesses()

    def get_wrong_guesses(self):
        return self.player.get_wrong_guesses()

    def display_spaces(self, guessed_letters):
        display = []
        for letter in self.word.get_word():
            if (letter in guessed_letters):
                display.append(letter)
            else:
                display.append("_")
        return " ".join(display)
    def draw_body_part(self):
        body_parts = [
"""
  +---+
  |   |
      |
      |
      |
      |
=========
""",
"""
  +---+
  |   |
  O   |
      |
      |
      |
=========
""",
"""
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
""",
"""
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
""",
"""
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
""",
"""
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
""",
"""
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
""",
]

        print body_parts[self.get_wrong_guesses()]

    def is_winner(self):
        return self.player.is_winner()

    def set_winner(self):
        self.player.set_winner()

    def get_wrong_letters(self):
        return self.player.get_wrong_letters()

    def increment_wrong_guesses(self):
        self.player.increment_wrong_guesses()

    def get_guessed_letters(self):
        return self.player.get_guessed_letters()

    def prompt_user(self):
        self.player.make_guess()
        return self.player.get_guess()

    def evaluate_guess(self, guess):
        letter_found = False
        for letter in self.get_word():
            if (letter == guess[0]):
                letter_found = True
        if (not letter_found):
            self.get_wrong_letters().append(guess)
            self.increment_wrong_guesses() #####finishhh

    def display_wrong_guesses(self):
        print "Wrong Guesses:"
        if (len(self.get_wrong_letters()) == 0):
            return "None"
        else:
            return " ".join(self.get_wrong_letters())

    def does_user_win(self):
        if (self.get_word() == "".join(self.display_spaces(self.get_guessed_letters())).replace(" ", "")):
                print "The word is:", self.display_spaces(self.get_guessed_letters()).replace(" ", "")
                print "You win!"
                self.set_winner()

    def final_guess(self):
        if (not self.player.is_winner()):
                print "You are out of guesses..."
                word_guess = raw_input("Enter word guess: ")
                if (word_guess == self.get_word()):
                        print "Correct... You Win!"
                else:
                        print "Incorrect... You Lose!"

    def play(self):
        
        while ((self.get_guesses() < (len(self.get_word())+2)) and not self.is_winner() and self.get_wrong_guesses() < 6):
            self.gui.display_word(self.display_spaces(self.player.get_guessed_letters()))
            self.gui.display_wrong_letters(self.display_wrong_guesses())
            guess = self.prompt_user()
            self.evaluate_guess(guess)
            self.display_wrong_guesses()
            self.draw_body_part()
            self.does_user_win()
            self.increment_guesses()
            self.gui.mainloop()
        self.final_guess()

class HangmanGUI():
        def __init__(self):
                self.hGUI = Tk()
                self.hGUI.geometry('{}x{}'.format(750,250))
                self.hGUI.resizable(width=FALSE, height=FALSE)
                self.frame = Frame(self.hGUI, height=1, width=2)
                self.frame.pack()
                self.bottomframe = Frame(self.hGUI)
                self.bottomframe.pack(side=BOTTOM)
                self.frames = []

                # Passed hangman game

        def mainloop(self):
                self.hGUI.mainloop()

        def create_frames(self):
                for x in range(0,3):
                        frame = Text(self.frame, height=10, width=25)
                        frame.pack(side=LEFT)
                        self.frames.append(frame)
                user_frame = Text(self.bottomframe, height=2, width=25)
                user_frame.pack(side=BOTTOM)
                self.frames.append(user_frame)
                
        def create_button(self):
                self.user_button = Button(self.bottomframe, text="Press to submit letter", command=self.get_user_input)
                self.user_button.pack( side = RIGHT)

        def get_user_input(self):
                self.user_input = self.frames[3].get("1.0", END)
                return self.user_input

        def display_word(self, word):
                self.frames[0].insert("1.0", word)

        def display_wrong_letters(self, wrong_letters):
                self.frames[1].insert("1.0", wrong_letters)

        def display_character(self):
                self.frames[2].insert("1.0", 'here is my text to insert')

class Player():
    def __init__(self):
        self.guesses = 0
        self.guess = None
        self.winner = False
        self.guessed_letters = []
        self.wrong_letters = []
        self.wrong_guesses = 0

    def get_guesses(self):
        return self.guesses

    def get_wrong_letters(self):
        return self.wrong_letters

    def increment_wrong_guesses(self):
        self.wrong_guesses += 1

    def increment_guesses(self):
        self.guesses += 1

    def make_guess(self):
        invalid_guess = True
        while (invalid_guess):
            self.guess = raw_input("Guess a letter: ")
            self.guess = self.guess.lower()
            if (self.guess not in self.guessed_letters):
                self.guessed_letters.append(self.guess)
                invalid_guess = False
            else:
                print "You already guessed that!"

    def get_guess(self):
        return self.guess[0]

    def get_wrong_guesses(self):
        return self.wrong_guesses

    def set_winner(self):
        self.winner = True

    def is_winner(self):
        return self.winner

    def get_guessed_letters(self):
        return self.guessed_letters

class Word():
    def __init__(self):
        self.word = "irobot"
        self.word = self.word.lower()

    def get_word(self):
        return self.word

    def word_length(self):
        return len(self.word)

def main():
    hangman = Hangman()
    hangman.play()

'''
gui = HangmanGUI()
gui.create_button()
gui.create_frames()
gui.display_word()
gui.display_wrong_letters()
gui.display_character()
gui.mainloop()
'''

if __name__ == "__main__":
    main()
