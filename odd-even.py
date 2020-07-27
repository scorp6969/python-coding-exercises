"""
Write a function called showNumbers that takes a parameter called limit.
It should print all the numbers between 0 and limit with a label to
identify the even and odd numbers. For example, if the limit is 3, it should print:
0 EVEN
1 ODD
2 EVEN
3 ODD
"""


def show_numbers(limit):
    for i in range(1, limit + 1):
        # print(i)
        if i % 2 == 0:
            print(f'{i} -> EVEN')
        else:
            print(f'{i} -> ODD')


lim = int(input('Enter the limit number : '))
show_numbers(lim)

