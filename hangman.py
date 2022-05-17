# """
#   Logan Morris
#   15 May 2022
#   Hangman game implementation with visual
# """
# Import statements
import random
from words import word_list # Import the words from the word list file

# Get the word from the word list
# Return it as a fully uppercase word
def get_word():
  word = random.choice(word_list)
  return word.upper()


def play(word):
  word_completion = "_" * len(word)
  guessed = False
  guessed_letters = []
  guessed_words = []
  tries = 6
  print("Welcome to Hangman!")
  print(display_hangman(tries))
  print(word_completion)
  print("\n")
  while not guessed and tries > 0:
    guess = input("Guess a letter or word: ").upper()
    # If the user guesses a letter
    if len(guess) == 1 and guess.isalpha():
      # If the letter is already guessed
      if guess in guessed_letters:
        print("You already guessed the letter", guess)
      # If the letter is not in the word
      elif guess not in word:
        print(guess, "is not in the word!")
        tries -= 1
        guessed_letters.append(guess)      
      # If the letter is a correct guess
      else:
        print("Good job,", guess, "is in the word!")
        guessed_letters.append(guess)
        word_as_list = list(word_completion) # make list for word to iterate
        indicies = [i for i, letter in enumerate(word) if letter == guess]
        # Iterate over the word and place all the correct guesses
        for index in indicies:
          word_as_list[index] = guess
        word_completion = "".join(word_as_list)
        if "_" not in word_completion:
          guessed = True
    # If the user guesses a word
    elif len(guess) == len(word) and guess.isalpha():
      # If the user has already guessed the word they inputted
      if guess in guessed_words:
        print("You already guessed the word", guess)
      
      # If the guess from the user is not the word
      elif guess != word:
        print(guess, "is not the word!")
        tries -= 1
        guessed_words.append(guess)

      # If the guess from the user is correct
      else:
        guessed = True
        word_completion = word

    # If the user has an invalid input
    else:
      print("Not a valid guess, please try again.")

    # Print out visual display
    print(display_hangman(tries))
    print(word_completion)
    print("\n")

  # Message if the user wins
  if guessed:
    print("Congrats, you guessed the word correctly! You win!")

  # Message if the user loses
  else:
    print("Sorry you ran out of guesses, the word was " + word + "Better luck next time!")

# Function making the display from the number of tries remaining
def display_hangman(tries):
  stages = [  # final state: head, torso, both arms, and both legs
              """
                  --------
                  |      |
                  |      O
                  |     \\|/
                  |      |
                  |     / \\
                  -
              """,
              # head, torso, both arms, and one leg
              """
                  --------
                  |      |
                  |      O
                  |     \\|/
                  |      |
                  |     / 
                  -
              """,
              # head, torso, and both arms
              """
                  --------
                  |      |
                  |      O
                  |     \\|/
                  |      |
                  |      
                  -
              """,
              # head, torso, and one arm
              """
                  --------
                  |      |
                  |      O
                  |     \\|
                  |      |
                  |     
                  -
              """,
              # head and torso
              """
                  --------
                  |      |
                  |      O
                  |      |
                  |      |
                  |     
                  -
              """,
              # head
              """
                  --------
                  |      |
                  |      O
                  |    
                  |      
                  |     
                  -
              """,
              # initial empty state
              """
                  --------
                  |      |
                  |      
                  |    
                  |      
                  |     
                  -
              """
  ]
  return stages[tries]

# Main function to run the game
def main():
  word = get_word()
  play(word)

  # Allow the user to continue playing
  while input("Play again? (Y/N) ").upper() == "Y":
    word = get_word()
    play(word)

# Allow for program to be run from the terminal
if __name__ == "__main__":
  main()