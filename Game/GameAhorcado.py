import random
import os


def run():
    
    IMAGES = ['''
        +---+
        |   |
            |
            |
            |
            |
        =========''', '''
        +---+
        |   |
        O   |
            |
            |
            |
        =========''', '''
        +---+
        |   |
        O   |
        |   |
            |
            |
        =========''', '''
        +---+
        |   |
        O   |
       /|   |
            |
            |
        =========''','''
        +---+
        |   |
        O   |
       /|\  |
            |
            |
        =========''','''
        +---+
        |   |
        O   |
       /|\  |
       /    |
            |
        =========''', '''
        +---+
        |   |
        O   |
       /|\  |
       / \  |
            |
        =========''']

    DB = [
        "TESTING",
        "PYTHON",
        "PROGRAMMING",
        "CODE",
        "RANDOM"
    ]
    
    Word = random.choice(DB)
    Spaces = ("_") * len(Word)
    attemps = 6
    
    while True:
        os.system("cls") # Clear the screen for Windows
        for character in Spaces:
            print(character, end=" ")
            print(IMAGES[attemps])
        letter =  input("Elige una letra: ").upper()
        
        found = False
        for idx, character in enumerate(Word):
            if character == letter:
                Spaces[idx] = letter
                found = True
                
            if not found:
                attemps -= 1
                
            if "_" not in Spaces:
                os.system("cls")
                print("Felicidades! Has ganado.")
                break
                input()
               
            if attemps == 0:
                os.system("cls")
                print("Perdiste.")
                break
                input()   
      
    if __name__ == '__main__':
        run()