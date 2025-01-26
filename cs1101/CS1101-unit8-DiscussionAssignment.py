try:
    rslt = open('read_text.txt', 'r')
    rslt.write('write process add')
except FileNotFoundError:
    print('File is not found !!')
except PermissionError:
    print("You aren't permitted to access to this file!!!")
except OSError:
        print("An os error has occurred")