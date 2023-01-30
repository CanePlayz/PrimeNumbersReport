import time

def sieve (n):
    prime = [True for i in range (n + 1)]
    p = 2
    while (p * p <= n):
        if (prime [p]):
            for i in range (p * p, n, p):
                prime [i] = False
        p += 1
    primeList = []
    c = 1
    for j in range (1, len (prime) - 1):
        if prime [j]:
            primeList.append (c)
        c += 1
    return primeList

def main (limit):
    start_time = time.time ()
    primes = sieve (limit)
    return (time.time () - start_time, primes)