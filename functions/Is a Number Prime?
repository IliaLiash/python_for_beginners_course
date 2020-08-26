#"True" if the number is prime or "False" otherwise
def is_prime(num):
    count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            count += 1
    if num <= 1:
        return False
    elif count <= 2:
        return True
    else:
        return False

n = int(input())

print(is_prime(n))
