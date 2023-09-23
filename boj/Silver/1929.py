n, m = map(int, input().split())

def isPrime(num):
    root = int(num ** 0.5)
    for i in range(2, root + 1):
        if num % i == 0:
            return False
    return True

for num in range(n, m + 1):
    if isPrime(num) and num != 1:
        print(num)