import random
import string
from words import words


def getValidWord(words):
    word = random.choice(words) #randomly chooses a word from the list

    while '-' in words or ' ' in word: #if word contains - or blankspace it just looks for another one
        word = random.choice(words)

    return word.upper()


def main():
    word = getValidWord(words)
    wordLetters = set(word)
    abc = set(string.ascii_uppercase)
    guessedLetters = set()

    lives = 11

    while len(wordLetters) > 0 and lives > 0:
        #prints already used letters
        print('\n\n\n\n\n\n\nLives left: ', lives)
        print('Already used letters: ', ' '.join(guessedLetters))

        print(displayHangman(lives))

        #prints the word encrypted only showing the already guessed letters (ie: W - R D)
        encryptedWord = [letter if letter in guessedLetters else '-' for letter in word]
        print('Current word: ', ' '.join(encryptedWord))

        userInput = input("Guess a letter: ").upper()
        if userInput in abc - guessedLetters:
            guessedLetters.add(userInput)
            if userInput in wordLetters:
                wordLetters.remove(userInput)
            else:
                lives-=1
                print("That letter is not in the word")

        elif userInput in guessedLetters:
            print("\nYou have already used that letter")

        else:
            print("\nWrong character. Try again")

    if lives > 0:
        print('YAY!!!!!!! You guessed the word ', word, ' and with ', lives, 'lives left!!!!!!')
    else:
    
        print('\n\n\n\n\n\n\n\n', displayHangman(lives))
        print('Sorry, you failed. The word was ', word)


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