def countup(n):
    if n >= 0:
        print("Blastoff! ")
    else:
        print(n)
        countup(n + 1)

def countdown(n):
     if n <= 0:
          print('Blastoff!')
     else:
          print(n)
          countdown(n-1)


def input_number():
    print("input the number")
    n = int(input())
    if n <= 0:
        countup(n)
    else:
        countdown(n)

def devide_two_value():
    print("From now on, I will do the division. " \
    "Please enter A in the value of A÷B.")
    A = int(input())
    print("Next, please enter B in the value of A÷B.")
    B = int(input())
    if B == 0:
        print('0 was entered in B. This will result in an error,' \
        'but I will calculate it just to be sure.')
    try:
        quotient = A // B
        remainder = A % B
    except ZeroDivisionError:
        print('This is ZeroDivisionError. Please do not enter zero into B.' \
        ' Please try again!!')
        devide_two_value()
    print(f'Done. The calculation quotient is {quotient} and remainder is {remainder}')


