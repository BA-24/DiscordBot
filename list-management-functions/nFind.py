def nFind(message):
    try:
        x = open('notes.txt', 'r')
        notes = x.readlines()
        x.close()
        for x in range(len(notes)):
            if message in notes[x]:
                return [True, x]
        
    except Exception as error:
        return [False, 'Error in nFind: ' + str(error)]
