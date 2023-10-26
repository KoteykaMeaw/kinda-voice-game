from speach import speach   
from random import choice
import time



levels = {

    "easy": ["dairy", "mouse", "computer"],

    "medium": ["programming", "algorithm", "developer"],

    "hard": ["neural network", "machine learning", "artificial intelligence"]

}

def play_game(level):

    words = levels.get(level,[])

    score = 0

    for _ in range(len(words)):
        randomword = choice(words)
        print(f'Произнесите слово {randomword}')
        recogword = speach()
        print(recogword)

        if randomword == recogword:
            print('Абсолютно верно!')
            score += 1
        else:
            print(f'Что то не получилось. Правильное слово : {randomword}')
        
        print(f'Игра завершена! Ваш счет : {score}/{len(words)}')

selectedlevel = input('Выберите уровень сложности(easy/medium/hard): ').lower()
play_game(selectedlevel)
            
    
