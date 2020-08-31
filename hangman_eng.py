from random import*
word_list = ['KEY', 'BOOK', 'RACCOON', 'CAR', 'COW', 'TROLLEY', 'HELMET', 'BUTTON', 'CORD', 'BLACK',
'VLASTERIN', 'SKYPE', 'OAK', 'CLOCK', 'PIPE', 'FIR-TREE', 'INSTITUTE', 'BOX', 'PLATE', 'WATER', 'FAN',
'MULTIPOINT', 'JEW', 'THERMIT', 'KACHEK', 'ROLL', 'RECORDER', 'LEG', 'ELEPHANT', 'MICROWAVE', 'CAKE', 'MAC',
'SMOKE', 'Gull', 'Jack', 'Skirting', 'Hat', 'Dinosaur', 'Torsher', 'Balalaika', 'BANK', 'Yacht', 'Sheep', 'BANANA',
'OAK', 'ANIME', 'RAINBOW', 'LETTER', 'BICYCLE', 'BANJO', 'DOVE', 'RIFLE', 'CUP', 'JASMINE', 'TELEPHONE',
'ANDROID', 'MOUNTAIN', 'BOTTLE', 'TOKEN', 'RIM', 'SOAP', 'YOG', 'BUMP', 'DOLLAR', 'COLUMN', 'CUBE', 'OMAR',
'ROCKET', 'CARROT', 'MIRROR', 'HAMMER', 'AIR', 'SNAKE', 'HEDGEHOG', 'PALM', 'OIL', 'DJ', 'BAG', 'TUBE',
'BRAIN', 'TRAIN', 'SOCKET', 'PARCHUTIST', 'PROTEIN', 'SPROTS', 'DUMP', 'PUZZLE', 'BOTTLE', 'KREMLIN', 'PIZZA',
'PASTA', 'CARPET', 'TEETH', 'LABEL', 'KASHALOT', 'MARS', 'JACKAL', 'LIPSTICK', 'JEEP', 'BREAM', 'STONE', 'DISC']

def get_word(word_list):
    word = choice(word_list).upper()
    return word

def display_hangman(tries):
    stages = [  
                    '''
                       --------
                       |      |
                       |      O
                       |     \\|/
                       |      |
                       |     / \\
                       -
                    ''',
                   
                    '''
                       --------
                       |      |
                       |      O
                       |     \\|/
                       |      |
                       |     / 
                       -
                    ''',
                   
                    '''
                       --------
                       |      |
                       |      O
                       |     \\|/
                       |      |
                       |      
                       -
                    ''',
                    
                    '''
                       --------
                       |      |
                       |      O
                       |     \\|
                       |      |
                       |     
                       -
                    ''',
                    
                    '''
                       --------
                       |      |
                       |      O
                       |      |
                       |      |
                       |     
                       -
                    ''',
                    
                    '''
                       --------
                       |      |
                       |      O
                       |    
                       |      
                       |     
                       -
                    ''',
                    
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
    word_completion = '_ ' * len(word)  
    guessed = False                    
    guessed_letters = []               
    tries = 6                          
    
    print("Let's play hangman!")
    print(display_hangman(6))
    print(word_completion, 'There are', len(word), 'letters in the hidden word')
    
    while True:
        print('\n'*2, 'Enter a letter or the whole word: ', sep='', end='')
        word_input = input().upper()
        if word_input == word:
            print('\n', "---Congrat's, you guessed the word ", word, " !---", sep='')
            break 
        
        if word_input.isalpha() == False:
            print('Please enter a letter or whole word')
            continue
        
        if word_input in guessed_letters:
            print('You have already entered this letter')
            continue
        
        if len(word_input) >= 2:
            print('Please enter a letter or whole word')            continue        
        
        else:               
            if tries == 0:
                print("You didn't guess the word", word)
                break               
            
            if word_input not in word and len(word_input) == 1:
                tries -= 1
                print('\n', 'This letter is not in the word, you have ', tries, ' attempts left', sep='')
                guessed_letters.append(word_input)                
                print(display_hangman(tries))                   
                
            if word_input in word and len(word_input) == 1:
                guessed_letters.append(word_input)                
                print('\n', 'Great, this letter is in the word!', sep='')
                if set(guessed_letters) == set(word):
                    print('\n' * 2, "---Congrat's, you guessed the word ", word, " !---", sep='')
                    guessed == True
                    break  
                else:
                    for element in word:
                        if element in guessed_letters:
                            print(element, end=' ')
                        else:
                            print('_', end=' ')                                 
                        
play(get_word(word_list))