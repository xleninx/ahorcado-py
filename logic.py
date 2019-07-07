from data import IMAGES, WORDS, LOSE_MESSAGE, WIN_MESSAGE
import random
import os 

def ramdom_word():
    idx = random.randint(0, len(WORDS) - 1)
    return WORDS[idx]

def display_board(hidden_word, tries):
    os.system('clear')
    print('Bienvenido al Ahorcado')
    print(IMAGES[tries])
    print('')
    print(hidden_word)

def you_lose():
    os.system('clear')
    print(LOSE_MESSAGE)

def you_win():
    os.system('clear')
    print(WIN_MESSAGE)

def fill_hidden_word(word, found_letters):
    hidden_word = []
    for letter in word:
        if letter in set(found_letters):
            hidden_word.append(letter)
        else:
            hidden_word.append('-')
    return hidden_word

def run():
    word = ramdom_word()
    hidden_word = ['-'] * len(word)
    found_letters = set()
    tries = 0

    while True:
        hidden_word = fill_hidden_word(word, found_letters)
        display_board(hidden_word, tries)
        letter = str(input('Ingresa una letra: '))
        if letter in word:
            found_letters.add(letter)
            
            if len(found_letters) == len(set(word)): 
                you_win()
                break
        else:
            tries += 1
            if tries >= len(IMAGES) - 1:
                you_lose()
                break

if __name__ == '__main__':
    run()