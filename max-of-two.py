# Write a function that returns the maximum of two numbers.


def max_of_two(x, y):
    if x > y:
        print(f'{x} is the biggest number')
    else:
        print(f'{y} is the biggest number')


num1 = int(input('Enter First Number : '))
num2 = int(input('Enter Second Number : '))

max_of_two(num1, num2)
