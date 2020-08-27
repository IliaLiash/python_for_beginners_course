from random import*
new_game = True

while new_game:
    print('Welcome to quessing game!')
    print('Enter the border "n" [1, n]:', end=' ')
    n = int(input())
    num = randint(1,n)

    def is_valid(number):
        global n
        return 1 <= number <= n

    print('Enter your number:', end=' ')
    find_number = int(input())
    count = 0

    while find_number != num:
    
        if is_valid(find_number):
            if find_number < num:
                print('Your number is less than the guessed one, try again')
                find_number = int(input())
                count += 1
            elif find_number > num:
                print('Your number is more than the guessed one, try again')
                find_number = int(input())
                count += 1
               
        else:
            print('Maybe enter integer from 1 to ', n, '?', sep='')
            find_number = int(input())
            count += 1

    if find_number == num:
        print('Yes! It is ', num, '!', sep='')
        print('Congrats, You guessed that number on the', count + 1, 'try!!')
        print('Do you wanna try once more? (Y, N)')
    
    answer = input()
    if answer == 'Y':
        new_game = True
        print('-' * 25)  
    else:
        new_game = False
        print('Thanks for playing the guessing game!')
