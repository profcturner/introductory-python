# Work with numbers - this is highly unpolished!
# But may help.

def divisors(n):
    """Return a list of all divisors (factors) of n"""

    # Make a list for the results
    results = []

    # Check all the numbers from 1 to n inclusive
    for m in range(1, n+1):
        # If there is no remainder when n is divided by m
        if n % m == 0:
            # Then m is a factor
            results.append(m)

    return(results)


def prime_numbers(n):
    """A primitive routine for returning a list of prime numbers up to n"""

    # Make a list for the results
    results = []
    
    # As before, check all the integers up to n inclusive
    for m in range(1, n+1):
        # Prime numbers have exactly two divisors
        if len(divisors(m)) == 2:
            # m is Prime
            results.append(m)

    return(results)

def prime_factors(n):
    """Only return factors of n that are prime"""

    # Make a list for the results
    results = []

    # Get all the factors
    factors = divisors(n)

    # Check each
    for m in factors:
        if len(divisors(m)) == 2:
            # Yes, it's prime
            results.append(m)

    return(results)

def check_pythagorean_triple(a, b, c):
    # For now, assume c is the largest
    if a*a + b*b == c*c:
        return True
    else:
        return False

def generate_pythagorean_triples(n):
    """Generate Pythagorean triples with x,y,z less than n"""
    # We could improve this a lot!

    # Let x be the smallest...
    for x in range(1, n+1):
        # y can go from x to n
        for y in range(x+1, n+1):
            # Let z step from y+1 upwards till we get perfect squares
            z = y + 1
            while z * z < x * x + y * y:
                z = z + 1
            if z * z == x * x + y * y and z <= n:
                print(x,y,z)

def Fibonacci(n):
    """Generate Fibonacci numbers up to and including n"""

    # Make a list for the results, add the first two terms
    results = [1, 1]

    # Starts with 1 and 1, each number is the sum of the two before it.
    a = 1
    b = 1
    c = a + b

    while c <= n:
        # Add it to the list
        results.append(c)

        # Caterpillar along - drop smallest number a
        a = b
        b = c
        c = a + b
        

    return(results)
    
        


def main():

    n = int(input("Please specify a positive integer: "))

    print("The divisors for", n, "are", divisors(n))
    print("The prime numbers up to",n,"are", prime_numbers(n))
    print("The prime divisors for", n, "are", prime_factors(n))

    print("3, 4, 5 is a Pythagorean triple? ", check_pythagorean_triple(3,4,5))
    print("3, 4, 6 is a Pythagorean triple? ", check_pythagorean_triple(3,4,6))

    print("Pythagorean Triples with all sides less than or equal to",n,"are")
    generate_pythagorean_triples(n)

    print("Fibonacci sequence is ", Fibonacci(n))
    

main()
