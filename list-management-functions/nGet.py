def nGet(number, includeNumber):
    try:
        note = ''
        f = open('notes.txt', 'r')
        wordlist = ''
        for r in f:    
            if r != '\n':
                wordlist = wordlist + r.split()[0]
        f.close()
        
        noteNumbers = list(str(wordlist))
        with open('notes.txt', 'r') as f:
            notes = f.readlines()

        for x in range(len(notes)):
            if includeNumber == False:
                notes[x] = notes[x].replace(noteNumbers[x], '', 1)
                notes[x] = notes[x].replace(' ', '', 1)
                notes[x] = notes[x].replace('\n', '', 1)

        for x in range(len(noteNumbers)):
            if str(number) == noteNumbers[x]:
                note = notes[x]
                return [True, note]
            
        if note == '':
            return [True, None]
    
    except Exception as error:
        return [False, 'Error in nGet: ' + str(error)]
