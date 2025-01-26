def operate_list(in_a:list, in_b:list):
    try:
        integrate_list = zip(in_a,in_b,strict=True)
        for key, value in enumerate(integrate_list):
            print(str(key) + ":" + str(value))
    except ValueError:
        print("Please enter lists of the same length!!!")

def operate_dict(in_d:dict):
    for key, value in in_d.items():
        print(str(key) + ":" + str(value))

a = ["a","b","c","d","e"]
c = ["a","b","c","d","e", "f"]
b = ["A","B","C","D","E"]
d = {"a": 1, "b": 3, "c": 7}
operate_list(a,b)
operate_list(c,b)
operate_dict(d)