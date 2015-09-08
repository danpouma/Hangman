def drawBodyPart(wrong_guesses):
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

	print body_parts[wrong_guesses]
	
def displaySpaces(guessed_letters):
        d_word = []
        for letter in word:
                if (letter in guessed_letters):
                        d_word.append(letter)
                else:
                        d_word.append("_")
        return " ".join(d_word)

word = "zockerz"

guesses = 0
#loop till length of word + 2 or till winner
while (guesses < (len(word)+2) and not winner):
        valid_guess = False
        
        print displaySpaces(guessed_letters)
        #add loop so you can't guess letter twice
        while (not valid_guess):
                #verify input is a letter
                guess = raw_input("Enter a letter: ")
                if (guess in guessed_letters):
                        print "You already guessed that letter."
                else:
                        guessed_letters.append(guess)
                        valid_guess = True
        letter_found = False
        for letter in word:
                #guess[0] to verify one letter
                if (letter == guess[0]):
                        letter_found = True
                        
        if (not letter_found):
                wrong_letters.append(guess)
                wrong_guesses += 1
                
        print "Wrong guesses:"
        if (len(wrong_letters) == 0):
                print "None"
        else:
                print " ".join(wrong_letters)
                
        guesses += 1
        drawBodyPart(wrong_guesses)

        
        
        if (word == "".join(displaySpaces(guessed_letters)).replace(" ", "")):
            print displaySpaces(guessed_letters)
            print "You win"
            winner = True

if (not winner):
        print "You are out of guesses..."
        word_guess = raw_input("Enter word guess: ")
        if (word_guess == word):
                print "you guessssede correctlyyyy"
        else:
                print "you lose"
