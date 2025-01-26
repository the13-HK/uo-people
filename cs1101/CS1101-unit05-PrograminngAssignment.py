def analizeName(n:str):
    print('Your name is ' + n)
    vowels = 'aeiou'
    countVowel = 0
    reverseName = ''
    for i in reversed(n):
        if i in vowels:
            countVowel += 1
        else:
            pass
        reverseName = reverseName + i
    print('Your name contains ' + str(countVowel) + 'vowels')
    print('Reversed name is ' + reverseName)