import math

def calc_hypotenuse (leg1, leg2):
    if not (is_num(leg1) and is_num(leg2)):
        return ("Argument should input int or float, and over zero")

    answer = calc_pythagoream_teorem (leg1, leg2)
    return answer


def is_num(n):
    if isinstance(n, int) or isinstance(n, float):
        if n > 0:
            return True
    return False

def calc_pythagoream_teorem (num1, num2):
    power_num = num1 ** 2 + num2 ** 2
    num2 = math.sqrt(power_num)
    return num2


def calc(arg = 0, recursion = False):

    if recursion:
        print("input symbol")
        m = input()
        if m == "=":
            print("result is " + str(arg))
            return arg
    else:
        m = ""
    print("input some number")
    n = int(input())
    if not is_num(n):
        calc()
    if m == "+":
        calc(arg + n, True)
    elif m == "-":
        calc(arg - n, True)
    elif m == "/":
        calc(arg /n, True)
    elif m == "*":
        calc(arg * n, True)
    elif m == "":
        calc(n, True)
    else:
        print("input some wrong symbol")