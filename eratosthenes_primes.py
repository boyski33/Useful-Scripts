# my algorithm
def prime_numbers(n):
    if n >= 2:
        primes = [2,]
    else:
        return 0

    outer_cont = False

    for num in range(3, n+1):
        for p in primes:
            ## withouth the next if block, it's 13 times slower
            if p > math.sqrt(num):
                break
            ##
            if num % p == 0:
                outer_cont = True
                break

        if outer_cont:
            outer_cont = False
            continue

        primes.append(num)

    return primes

# really smart algorithm -- about 3-4 times faster than mine
def prime_sieve2(n):
    not_prime = set()
    primes = []

    for i in range(2, n + 1):
        if i in not_prime:
            continue

        for f in range(i * 2, n + 1, i):
            not_prime.add(f)

        primes.append(i)
        print(i)

    return primes
