#Write a program that reverses and prints the sequence of characters enclosed between the first and last occurrences of the letter "h".

s = input()

print(s[:s.find('h')], s[s.rfind('h'):s.find('h'):-1], s[s.rfind('h'):], sep='')
