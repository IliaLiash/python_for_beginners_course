#You need to print the same lines, but remove comments and white space characters at the end of lines

list1 = input().split('#')
list_txt = []
n = int(list1[1])

for string in range(n):
    string = input()
    if '#' in string:
        list_txt.append(string[:string.index('#')].rstrip())
    else:
        list_txt.append(string.rstrip())

print(*list_txt, sep='\n')
