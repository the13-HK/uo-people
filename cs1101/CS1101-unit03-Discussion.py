def unit3_discussion_forum_chained(target:int):
    if target % 24 == 0:
        print(24)
    elif target % 12 == 0:
        print(12)
    elif target % 8 == 0:
        print(8)
    elif target % 6 == 0:
        print(6)
    elif target % 4 == 0:
        print(4)
    elif target % 3 == 0:
        print(3)
    elif target % 2 == 0:
        print(2)
    else:
        print(1)

def unit3_discussion_forum_nested(target:int):
    if target % 3 == 0:
        target = target // 3
        if target % 2 == 0:
            target = target // 2
            if target % 2 == 0:
                target = target // 2
                if target % 2 ==0:
                    print(24)
                else:
                    print(12)
            else:
                print(6)
        else:
            print(3)
    else:
        if target % 2 == 0:
            target = target // 2
            if target % 2 == 0:
                target = target // 2
                if target % 2 == 0:
                    print(8)
                else:
                    print(4)
            else:
                print(2)
        else:
            print(1)
