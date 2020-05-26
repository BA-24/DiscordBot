def tAdd(msg):
    try:
        x = open('topics.txt', 'a')
        x.write(msg)
        x.close()
        return [True, None]
    except Exception as error:
        return [False, 'Error in tAdd: ' + str(error)]
