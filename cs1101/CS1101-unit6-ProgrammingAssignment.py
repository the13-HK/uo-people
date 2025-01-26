def operate_list(l:list, sarary:dict):


    subList1  = l[:5]
    subList2 = l[5:]
    subList2.append('Kriti Brown')
    subList1.pop(1)

    update_salary = {key:value*1.04 for key, value in salary.items()}
    salary_sorted = sorted(update_salary.items(), key=lambda x:x[1], reverse=True)
    print(subList1 + subList2)
    print(salary_sorted[:3])


l = [
    'Jamal Murray',
    'Mikal Bridges',
    'Bradley Beal',
    'Mikal Bridges',
    'Giannis Antetokounmpo',
    'Kevin Durant',
    'Jaren Jackson Jr.',
    'Jaylen Brown',
    'Kristaps Porziņģis',
    'LeBron James'
]
salary = {
    'Jamal Murray': 36016200,
    'Mikal Bridges': 23300000,
    'Bradley Beal': 50203930,
    'RJ Barrett': 25794643,
    'Giannis Antetokounmpo':48787676,
    'Kevin Durant':51179020,
    'Jaren Jackson Jr.' :25257798,
    'Jaylen Brown' :49205800,
    'Kristaps Porziņģis' :29268293,
    'LeBron James' :48728845,
    'Kriti Brown' :12768664
}
operate_list(l, salary)
l.reverse()
operate_list(l, salary)







