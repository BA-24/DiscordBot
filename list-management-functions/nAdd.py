def nAdd(number, msg):
    try:
        number = str(number)
        x = open('notes.txt', 'a')
        x.write(number + ' ' + msg + '\n')
        x.close()
        return [True, None]
    except Exception as error:
        return [False, 'Error in nAdd: ' + str(error)]
