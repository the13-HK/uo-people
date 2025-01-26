def pa_unit7(inp_dict:dict):
    ret_dict = dict()
    for key, value in inp_dict.items():
        for item in value:
            if item not in ret_dict:
                ret_dict[item] = [key]
            else:
                ret_dict[item].append(key)
    return ret_dict
input_example = { 'Stud1': ['CS1101', 'CS2402', 'CS2001'], 'Stud2': ['CS2402','CS2001','CS1102'] }
nba_data = {'Giannis':['Buckes'], 'Lebron':['Cavs', 'Heat', 'Lakers'], 'Curry':['Warriors'],'Durant':['Thunder', 'Warriors', 'Nets','Suns'], 'Kyrie':['Cavs','Celtics','Nets','Mavs']}
output_dict = pa_unit7(input_example)
output_nba_dict = pa_unit7(nba_data)
print(output_dict)
print(output_nba_dict)