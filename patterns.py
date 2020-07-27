"""
Write a function called show_stars(rows).
If rows is 5, it should print the following:
*
**
***
****
*****
"""

# Alternative
# def show_stars(rows):
#     for i in range(0, rows + 1):
#         for j in range(0, i):
#             print('*', end="")
#         print('\r')


def show_star(rows):
    my_list = []
    for i in range(rows + 1):
        my_list.append('*' * i)
    print('\n'.join(my_list))


row = int(input('Enter row number : '))

# Alternative
# show_stars(row)

show_star(row)
