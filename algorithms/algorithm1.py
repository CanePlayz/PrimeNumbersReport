import time


def prime(n):
    if n == 1:
        return False
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
    return True


def main(limit):
    start_time = time.time()
    nums = range(1, limit)
    primes = list(filter(prime, nums))
    return (time.time() - start_time)
