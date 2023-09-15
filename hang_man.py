import random
from words import words
import string

def valid_words(words):
  word = random.choice(words)
  
  while '-' in word or ' ' in word:
    word = random.choice(words)
  return word.upper()
 

def hangman():
  word = valid_words(words) # a valid word from the words
  word_letters = set(word) # breaks the word into letters 
  alphabet = set(string.ascii_uppercase) # set if upper case letter is the alphabet 
  used_letters = set() # used letter from the user_input
  lives = 7


  #getting imput
  while len(word_letters) > 0 and lives != 0:
    print('----------\n')
    print(f'You have {lives} lives\n')
    print('you have used these letters: ', " ".join(used_letters))
    
    word_list = [letter if letter in used_letters else '-' for letter in word]
    print('current word: ', " ".join(word_list))

    user_input = input('\nGuess the letter: ').upper()

    if user_input in alphabet and user_input not in used_letters:
        used_letters.add(user_input)
  
        if user_input in word_letters:
            word_letters.remove(user_input)
        else:
           lives -= 1 
        
    elif user_input in used_letters:
        print("You already used that letter, choose another one")

    else:
        print('Invalid letter')

  if lives == 0:
    print(f'You lost! The words was {word}')
  if len(word_letters) == 0:
    print(f'You Won! the word is {word}')
  

  


hangman()