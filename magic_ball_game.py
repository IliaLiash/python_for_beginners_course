from random import*

answers = ["Undoubtedly", "It seems - yes", "It's not clear yet, try again", "Don't even think",
           "Foregone conclusion, ", "Most likely", "Ask later", "My answer is no",
           "No doubts", "Good prospects", "Better not to tell", "According to my information - no",
           "You can be sure of this", "Yes", "Concentrate and ask again", "Very doubtful"]
new_game = True


print('Hello World! I am a magic ball, and I know the answer to any of your questions!')
print('What is your name?', '\n')
name = input()

print('\n','Hello ', name, '!', sep='')
while new_game:
    print('Please ask your question...')
    print()
    question = input()

    print('\n','I think.... ', choice(answers), sep='')
    print('\n', 'Do you have any more questions, ', name, '? (Y or N)', sep='')

    ans = input()

    if ans == 'Y':
        new_game = True
        print()
    else:
        new_game = False
        print('Come back if you have any questions!')
