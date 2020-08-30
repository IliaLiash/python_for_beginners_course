from random import*
word_list = []

def get_word():
    word = choice(word_list).upper()

def display_hangman(tries):
    stages = [  # ��������� ���������: ������, ����, ��� ����, ��� ����
                    '''
                       --------
                       |      |
                       |      O
                       |     \\|/
                       |      |
                       |     / \\
                       -
                    ''',
                    # ������, ����, ��� ����, ���� ����
                    '''
                       --------
                       |      |
                       |      O
                       |     \\|/
                       |      |
                       |     / 
                       -
                    ''',
                    # ������, ����, ��� ����
                    '''
                       --------
                       |      |
                       |      O
                       |     \\|/
                       |      |
                       |      
                       -
                    ''',
                    # ������, ���� � ���� ����
                    '''
                       --------
                       |      |
                       |      O
                       |     \\|
                       |      |
                       |     
                       -
                    ''',
                    # ������ � ����
                    '''
                       --------
                       |      |
                       |      O
                       |      |
                       |      |
                       |     
                       -
                    ''',
                    # ������
                    '''
                       --------
                       |      |
                       |      O
                       |    
                       |      
                       |     
                       -
                    ''',
                    # ��������� ���������
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
    word_completion = '_' * len(word)  # ������, ���������� ������� _ �� ������ ����� ����������� �����
    guessed = False                    # ���������� �����
    guessed_letters = []               # ������ ��� ��������� ����
    guessed_words = []                 # ������ ��� ��������� ����
    tries = 6                          # ���������� �������    
    
    print('Lets play hangman!')
    print(display_hangman(6))
    print(word_completion)
    
    while guessed != True:
        word_input = ('������� ����� ��� �����: ').upper()
        
        if word_input.isalpha() == False:
            print('����������, ������� ����� ��� �����')
            continue
        if word_input in quessed_words:
            print('�� ��� �������� ��� �����')
            continue
        if word_input in guessed_letters:
            print('�� ��� �������� ��� �����')
            continue
        
        else:
            if word_input not in word and len(word_input) > 1:
                tries -= 1
                guessed_word.append(word_input)
                print('��� �� ���������� �����, � ��� ��������', tries, '�������')
            
            if word_input not in word and len(word_input) == 1:
                tries -= 1
                guessed_letters.append(word_input)                
                print('���� ����� ��� � �����, � ��� ��������', tries, '�������')
                
            if word_input in word and len(word_input) == 1:
                guessed_letters.append(word_input)                
                print('�������, ����� ����� ���� � �����!')
                for i in range(len(word)):
                    if word[i] != word_input:
                        print('_', sep='', end='')
                    else:
                        print(word_input, sep='', end='')
                        
            
                