#Write a program that prints the index of the second occurrence of the letter "f".
#If the letter "f" occurs only once, print the number -1, and if it doesn't occur, print the number -2.

s = input()
count = 0

if s.count('f') == 1:
    print('-1')
elif s.count('f') == 0:
    print('-2')
else:
    for i in range(len(s)):
        if s[i] == 'f':
            count += 1
        if count == 2:
            print(i)
            break
