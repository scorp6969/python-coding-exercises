"""
Write a function for checking the speed of drivers.
This function should have one parameter: speed.
If speed is less than 70, it should print “Ok”.
Otherwise, for every 5km above the speed limit (70),
it should give the driver one demerit point and print the total number of demerit points.
For example, if the speed is 80, it should print: “Points: 2”.
If the driver gets more than 12 points, the function should print: “License suspended”
"""


def speed_check(speed):
    s = 70
    points = round((speed - s) / 5)
    if speed == s:
        print('OK !')
    elif points >= 12:
        print(f'\nDemerits point is {points}.\nLicense suspended !!!')
    else:
        print(f'\nWarning !!!\nDemerits point = {points}')


user_speed = int(input('Enter Speed = '))
speed_check(user_speed)
