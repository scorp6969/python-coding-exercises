"""
Write a function that prints all the prime numbers
between 0 and limit where limit is a parameter.
"""


def prime_check(limit):
    for num in range(0, limit+1):
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                print(num)
    if num == 0 or num == 1:
        print(f'{num} is neither prime nor composite')


n = int(input('Enter the limit : '))
prime_check(n)
