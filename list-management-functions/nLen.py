def nLen():
    try:
        x = open('notes.txt', 'r')
        notes = x.readlines()
        x.close()
        return [True, len(notes)]
    
    except Exception as error:
        return [False, 'Error in nLen: ' + str(error)]
