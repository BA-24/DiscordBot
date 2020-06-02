def tnBackup(mode):
    try:
        if mode == 'save':
            f = open('notes.txt', 'r')
            notes = f.read()
            f.close()
            f = open('topics.txt', 'r')
            topics = f.read()
            f.close()
            f = open('./backup/notes.txt', 'w')
            f.write(notes)
            f.close()
            f = open('./backup/topics.txt', 'w')
            f.write(topics)
            f.close()
            return [True, 'save']
        elif mode == 'load':
            f = open('./backup/notes.txt', 'r')
            notes = f.read()
            f.close()
            f = open('./backup/topics.txt', 'r')
            topics = f.read()
            f.close()
            f = open('notes.txt', 'w')
            f.write(notes)
            f.close()
            f = open('topics.txt', 'w')
            f.write(topics)
            f.close()
            return [True, 'load']
        return [True, None]

    except Exception as error:
        return[False, error]
