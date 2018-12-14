N = 100
primes = []


def is_prime(num):
    for p in primes:
        if num % p == 0:
            return False
    return True


for i in range(2, N):
    if is_prime(i):
        primes.append(i)


for p in primes:
    print(p, end=" ")