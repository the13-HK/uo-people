import json
def load_file():
    try:
        input = open('input_file.json', 'r')
        input_json = json.load(input)
        print(input_json)
    except Exception as e:
        print(e)

    ret_dict = dict()
    for key, value in input_json.items():
        if type(value) is str:
            if value not in ret_dict:
                ret_dict[value] = [key]
            else:
                ret_dict[value].append(key)
        elif type(value) is list:
            for item in value:
                if item not in ret_dict:
                    ret_dict[item] = [key]
                else:
                    ret_dict[item].append(key)

    try:
        output = open('output_file.json', 'w')
        json.dump(ret_dict, output, indent=3)
    except Exception as e:
        print(e)

    return ret_dict

print(load_file())
