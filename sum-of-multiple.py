"""
Write a function that returns the sum of multiples of
3 and 5 between 0 and limit (parameter). For example,
if limit is 20, it should return the
sum of 3, 5, 6, 9, 10, 12, 15, 18, 20.
"""

num = []


def sum_of(limit):
    # s = 0
    for i in range(0, limit + 1):
        if i % 3 == 0 or i % 5 == 0:
            num.append(i)
            # s += i
    # print(f"Sum of numbers : {s}")


lim = int(input('Enter the limit : '))
sum_of(lim)
print('------ Numbers ------')
print(num)
print('---------------------')
print(f'Sum of numbers : {sum(num)}')
