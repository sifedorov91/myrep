import random
def hangman(word = ''):
    words = ['кот',
             'пёс',
             'мяч',
             'рис'
             ]
    random_index = random.randint(0, (len(words))-1)
    word = words[random_index]
    wrong = 0
    stages = ['',
              '_______         ',
              '|      |        ',
              '|      |        ',
              '|      O        ',
              '|     /|\       ',
              '|     / \       ',
              '|               '
            ]
    rletters = list(word)
    board = ['_'] * len(word)
    win = False
    print ('Добро пожаловать на казнь!')

    while wrong < len(stages)-1:
        print('\n')
        char = input('Введите букву: ')
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print(' '.join(board))
        e = wrong+1
        print('\n'.join(stages[0:e]))
        if '_' not in board:
            print('Вы выиграли! Было загадано слово: ')
            print(' '.join(board))
            win = True
            break
    if not win:
        print('\n'.join(stages[0:wrong]))
        print(f'Вы проиграли! Было загадано слово:{word}')
hangman()


