def tFind(message):
    try:
        f = open('topics.txt', 'r')
        topics = f.readlines()
        f.close()
        a = 0
        for x in topics:
            if message in x:
                return [True, a]
            a = a + 1
        return [True, None]

    except Exception as error:
        return [False, 'Error in tFind: ' + str(error)]
