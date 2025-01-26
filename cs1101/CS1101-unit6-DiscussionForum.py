def compare_list(list1:list, list2:list):
    if list1 is list2:
        print("lists which is inputted is identical")
    elif list1 == list2:
        print("lists which is inputted is equivalent")
    else:
        print("lists which is inputted isn't same")

def alter_list(original:list):
    l = len(original)
    breakjudge = True
    while breakjudge:
        print(
            f'input the index number you want to change, total range is {l}, ' \
            'if you want to exit, please enter -1'
        )
        n = int(input())
        if n == -1:
            breakjudge = False
            print(
                'It\'s done!'
            )
            continue
        elif n > l:
            print(
                f'Please input under {l}'
            )
        else:
            print(
                'Input the value number you want to change'
            )
            m = input()
            if is_int(m):
                original[n] = int(m)
            elif is_float(m):
                original[n] = float(m)
            else:
                original[n] = m

        print(
            f'Now, original list is {original}'
        )
def is_int(s:str):
    try:
        int(s)
    except ValueError:
        return False
    else:
        return True
def is_float(s:str):
    try:
        float(s)
    except ValueError:
        return False
    else:
        return True