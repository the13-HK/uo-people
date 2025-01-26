def is_EvenNumber(n:int):
    return True if n % 2 == 0 else False


def print_EvenOdd(n:int):
    print('Even' if is_EvenNumber(n) == 0 else 'Odd')