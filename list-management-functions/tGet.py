def tGet(number):
    try:
        f = open('topics.txt')
        topics = f.readlines()
        f.close()
        if number >= len(topics):
            return [True, None]
        else:
            if topics[number] == '' or topics[number] == '\n':
                return[True, None]
            else:
                return [True, topics[number].replace('\n', '', 1)]

    except Exception as error:
        return [False, 'Error in tGet: ' + str(error)]
