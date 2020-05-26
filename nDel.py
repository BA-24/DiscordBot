def nDel(number):
    try:
        note = nGet(number, True)
        if note[1] == None:
            return [True, None]
        else:
            x = open('notes.txt', 'r')
            notes = x.readlines()
            x.close()
            notes.remove(note[1])
            x = open('notes.txt', 'w')
            x.write("".join(notes))
            x.close()
            return [True, note[1]]
        
    except Exception as error:
        return [False, 'Error in nDel: ' + str(error)]
