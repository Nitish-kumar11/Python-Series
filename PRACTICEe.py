# function that returns a list of all prime numbers less than a given number.
def get_primes(n):
    primes = []
    for num in range(2, n):
        if all(num % i != 0 for i in range(2, int(num**0.5) + 1)):
            primes.append(num)
    return primes

print(get_primes(10))  
