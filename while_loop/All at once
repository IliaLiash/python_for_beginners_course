#sum of the digits;
#number of digits;
#product of numbers;
#arithmetic mean of digits;
#first digit;
#sum of the first and last digits.

num = int(input())
count = 0
total = 0
mult = 1
arithmetic = 0
summ_first_last = 0
last_digit1 = num % 10

while num != 0:   
    last_digit = num % 10
    count += 1
    total += last_digit
    mult *= last_digit
    arithmetic = total / count
    if num // 10 == 0:
        first_digit = last_digit
        summ_first_last = first_digit + last_digit1
    num = num // 10
print(total, count, mult, arithmetic, first_digit, summ_first_last, sep='\n')
