import random
import string
from language import english
from language import spanish
from words import words
from words import wordsEsp


def getValidWord(words):
    word = random.choice(words) #randomly chooses a word from the list

    while '-' in words or ' ' in word: #if word contains - or blankspace it just looks for another one
        word = random.choice(words)

    return word.upper()


def main():
   texts = {}
   lang = "n/a"
   abc = set(string.ascii_uppercase)
   while lang != 'esp' and lang != 'eng':
      lang = input('To play in English, type "eng"\nPara jugar en Español, introduce "esp"').lower()
   if lang == 'esp':
      texts = spanish
      word = getValidWord(wordsEsp)
      abc.add('Ñ')
   elif lang == 'eng':
      texts = english
      word = getValidWord(words)
   wordLetters = set(word)
   
   guessedLetters = set()

   lives = 11

   while len(wordLetters) > 0 and lives > 0:
      #prints already used letters
      print(texts['lifes'], lives)
      print(texts['used'], ' '.join(guessedLetters))

      print(displayHangman(lives))

      #prints the word encrypted only showing the already guessed letters (ie: W - R D)
      encryptedWord = [letter if letter in guessedLetters else '-' for letter in word]
      print(texts['word'], ' '.join(encryptedWord))

      userInput = input(texts['input']).upper()
      if userInput in abc - guessedLetters:
         guessedLetters.add(userInput)
         if userInput in wordLetters:
            wordLetters.remove(userInput)
         else:
            lives-=1
            print(texts['wrong'])

      elif userInput in guessedLetters:
         print(texts['repeated'])

      else:
         print(texts['wrongCharacter'])

   if lives > 0:
      print(texts['victory'].format(word, lives))
   else:
      print('\n\n\n\n\n\n\n\n', displayHangman(lives))
      print(texts['defeat'], word)


def displayHangman(lives):
   stages = [  # you failed
                """
                   --------
                   |/     |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                --------------
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |/     |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                --------------
                """,
                # head, torso, and both arms
                """
                   --------
                   |/     |
                   |      O
                   |     \\|/
                   |      |
                   |      
                --------------
                """,
                # head, torso, and one arm
                """
                   --------
                   |/     |
                   |      O
                   |     \\|
                   |      |
                   |     
                --------------
                """,
                # head and torso
                """
                   --------
                   |/     |
                   |      O
                   |      |
                   |      |
                   |     
                --------------
                """,
                # head
                """
                   --------
                   |/     |
                   |      O
                   |    
                   |      
                   |     
                --------------
                """,
                # rope
                """
                   --------
                   |/     |
                   |      
                   |    
                   |      
                   |     
                --------------
                """,
                # the structure
                """
                   --------
                   |/     
                   |      
                   |    
                   |      
                   |     
                --------------
                """,
                # floor and vertical and horizontal posts
                """
                   --------
                   |     
                   |      
                   |    
                   |      
                   |     
                --------------
                """,
                # floor and vetical post
                """
                   
                   |      
                   |      
                   |    
                   |      
                   |     
                --------------
                """,
                # just the floor
                """
                   
                         
                         
                       
                         
                       
                --------------
                """,
                # initial empty state
                """
                   
                         
                         
                       
                         
                        
                   
                """
   ]
   return stages[lives]


if __name__ == "__main__":
   main()