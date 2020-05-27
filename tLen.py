def tLen():
    try:
        f = open('topics.txt', 'r')
        topics = f.readlines()
        f.close()
        return [True, len(topics)]
    except Exception as error:
        return [False, 'Error in tLen: ' + str(error)]
