from Tkinter import *
import time


class HangmanGUI():
        def __init__(self):
                self.initialize_gui()
                self.hangman = Hangman()
                
        def initialize_gui(self):
                self.hGUI = Tk()
                self.hGUI.title("HANGMAN! by dan p")
                self.hGUI.geometry('{}x{}'.format(750,250))
                self.hGUI.resizable(width=FALSE, height=FALSE)
                self.frame = Frame(self.hGUI, height=1, width=2)
                self.frame.pack()
                self.bottomframe = Frame(self.hGUI)
                self.bottomframe.pack(side=BOTTOM)
                self.frames = []
                
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
                self.user_button = Button(self.bottomframe, text="Press to submit letter", command=self.play)
                self.user_button.pack( side = RIGHT)

        def get_user_input(self):
            invalid_guess = True
            if (invalid_guess):
                self.user_input = self.frames[3].get("1.0", END)
                self.hangman.player.set_guess(self.user_input)
                #self.hangman.player.add_guessed_letter(self.hangman.player.get_guess())
                if (self.hangman.player.get_guess() not in self.hangman.player.get_guessed_letters()):
                    self.hangman.player.get_guessed_letters().append(self.hangman.player.get_guess())
                    invalid_guess = False
                    self.hangman.player.increment_guesses()
                else:
                    print "You already guessed that!"
            return self.hangman.player.get_guess()

        def display_word(self):
                # Clear text then re-add it
                self.frames[0].delete("1.0", END)
                self.frames[0].insert("1.0", "\n\n\n\n\n\n\n"+self.hangman.display_spaces(self.hangman.player.get_guessed_letters()))

        def display_wrong_letters(self):
                # Clear text then re-add it
                self.frames[1].delete("1.0", END)
                self.frames[1].insert("1.0", "\n\n\n\n\n\nWrong Guesses:\n"+self.hangman.display_wrong_letters()) #hack for now

        def display_character(self):
                # Clear text then re-add it
                self.frames[2].delete("1.0", END)
                self.frames[2].insert("1.0", self.hangman.draw_body_part())

        def display_final_guess(self):
                self.user_button["text"] = "Out of guesses... Enter final guess!"
                print "You are out of guesses..."
                word_guess = self.get_user_input()
                if (word_guess == self.hangman.word.get_word()):
                        self.display_you_win()
                else:
                        self.display_you_lose()

        def display_you_lose(self):
                for x in range(0,3):    
                        self.frames[x].delete("1.0", END)
                        self.frames[x].insert("1.0", "YOU LOSE")

        def display_you_win(self):
                for x in range(0,3):    
                        self.frames[x].delete("1.0", END)
                        self.frames[x].insert("1.0", "YOU WIN")

        def play(self):
                end = False
                #loop till guesses are out
                if ((self.hangman.player.get_guesses() < (len(self.hangman.word.get_word())+2)) and not self.hangman.player.is_winner() and self.hangman.player.get_wrong_guesses() < 6):
                        self.hangman.evaluate_guess(self.get_user_input())
                        self.hangman.does_user_win()
                        self.display_word()
                        self.display_wrong_letters()
                        self.display_character()
                if (self.hangman.player.get_wrong_guesses() >= 6):
                        self.display_you_lose()
                """
                if (self.hangman.player.is_winner()):
                        self.display_you_win()
                        
                if (self.hangman.player.get_wrong_guesses() >= 6):
                        self.display_you_lose()
                        
                if (not self.hangman.is_game_over() and not self.hangman.player.is_winner()):
                        # final guess.. change button to say it
                        self.display_final_guess()
                """
                # Insert code to end-game
                #self.hGUI.destroy()

class Hangman():
    def __init__(self):
        self.word = Word()
        self.player = Player()
        self.game_over = False

    def is_game_over(self):
        return self.game_over

    def does_user_win(self):
        if (self.word.get_word() == "".join(self.display_spaces(self.player.get_guessed_letters())).replace(" ", "")):
                print "The word is:", self.display_spaces(self.player.get_guessed_letters()).replace(" ", "")
                print "You win!"
                self.player.set_winner()

    def evaluate_guess(self, guess):
        letter_found = False
        for letter in self.word.get_word():
            if (letter == guess[0]):
                letter_found = True
        if (not letter_found):
            self.player.get_wrong_letters().append(guess)
            self.player.increment_wrong_guesses()

    def display_wrong_letters(self):
        #print "Wrong Guesses:" ***Figure out how to make this get returned as well.
        if (len(self.player.get_wrong_letters()) == 0):
            return "None"
        else:
            return " ".join(self.player.get_wrong_letters())

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

        return body_parts[self.player.get_wrong_guesses()]

    def display_spaces(self, guessed_letters):
        display = []
        for letter in self.word.get_word():
            if (letter in guessed_letters):
                display.append(letter)
            else:
                display.append("_")
        return " ".join(display)

class Player():
    def __init__(self):
        self.guesses = 0
        self.guess = None
        self.winner = False
        self.guessed_letters = []
        self.wrong_letters = []
        self.wrong_guesses = 0

    def set_winner(self):
        self.winner = True

    def is_winner(self):
        return self.winner

    def get_wrong_guesses(self):
        return self.wrong_guesses

    def increment_wrong_guesses(self):
        self.wrong_guesses += 1
        
    def set_guess(self, guess):
        self.guess = guess

    def get_guess(self):
        return self.guess[0]

    def get_guesses(self):
        return self.guesses

    def get_guessed_letters(self):
        return self.guessed_letters

    def add_guessed_letter(self, guessed_letter):
        self.guessed_letters.append(guessed_letter)

    def get_wrong_letters(self):
        return self.wrong_letters

    def increment_guesses(self):
        self.guesses += 1

class Word():
    def __init__(self):
        self.word = "irobot"
        self.word = self.word.lower()

    def get_word(self):
        return self.word

    def word_length(self):
        return len(self.word)

def main():
        gui = HangmanGUI()
        gui.create_button()
        gui.create_frames()

        gui.display_word()
        gui.display_wrong_letters()
        gui.display_character()

        gui.mainloop()

if __name__ == "__main__":
    main()

