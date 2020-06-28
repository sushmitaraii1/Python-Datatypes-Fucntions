# 9. Write a Python function that takes a number as a parameter and check the
# number is prime or not.
# Note : A prime number (or a prime) is a natural number greater than 1 and that
# has no positive divisors other than 1 and itself.


def prime_check(num):
    if num == 1:
        return "It is not a prime number."
    elif num == 2:
        return "It is not a prime number."
    else:
        for i in range(2, num):
            if num % i == 0:
                return "It is not a prime number."
            else:
                return "It is a prime number."


sample = int(input("Enter a number: "))

print(prime_check(sample))
