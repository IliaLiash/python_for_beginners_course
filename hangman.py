from random import*
word_list = []

def get_word():
    word = choice(word_list).upper()

def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
                    '''
                       --------
                       |      |
                       |      O
                       |     \\|/
                       |      |
                       |     / \\
                       -
                    ''',
                    # голова, торс, обе руки, одна нога
                    '''
                       --------
                       |      |
                       |      O
                       |     \\|/
                       |      |
                       |     / 
                       -
                    ''',
                    # голова, торс, обе руки
                    '''
                       --------
                       |      |
                       |      O
                       |     \\|/
                       |      |
                       |      
                       -
                    ''',
                    # голова, торс и одна рука
                    '''
                       --------
                       |      |
                       |      O
                       |     \\|
                       |      |
                       |     
                       -
                    ''',
                    # голова и торс
                    '''
                       --------
                       |      |
                       |      O
                       |      |
                       |      |
                       |     
                       -
                    ''',
                    # голова
                    '''
                       --------
                       |      |
                       |      O
                       |    
                       |      
                       |     
                       -
                    ''',
                    # начальное состояние
                    '''
                       --------
                       |      |
                       |      
                       |    
                       |      
                       |     
                       -
                    '''
        ]
    return stages[tries]
    
def play(word):
    word_completion = '_' * len(word)  # строка, содержащая символы _ на каждую букву задуманного слова
    guessed = False                    # сигнальная метка
    guessed_letters = []               # список уже названных букв
    guessed_words = []                 # список уже названных слов
    tries = 6                          # количество попыток    
    
    print('Lets play hangman!')
    print(display_hangman(6))
    print(word_completion)
    
    while guessed != True:
        word_input = ('Введите букву или слово: ').upper()
        
        if word_input.isalpha() == False:
            print('Пожалуйста, введите букву или слово')
            continue
        if word_input in quessed_words:
            print('Вы уже называли это слово')
            continue
        if word_input in guessed_letters:
            print('Вы уже называли эту букву')
            continue
        
        else:
            if word_input not in word and len(word_input) > 1:
                tries -= 1
                guessed_word.append(word_input)
                print('Это не загаданное слово, у Вас осталось', tries, 'попыток')
            
            if word_input not in word and len(word_input) == 1:
                tries -= 1
                guessed_letters.append(word_input)                
                print('Этой буквы нет в слове, у Вас осталось', tries, 'попыток')
                
            if word_input in word and len(word_input) == 1:
                guessed_letters.append(word_input)                
                print('Отлично, такая буква есть в слове!')
                for i in range(len(word)):
                    if word[i] != word_input:
                        print('_', sep='', end='')
                    else:
                        print(word_input, sep='', end='')
                        
            
                