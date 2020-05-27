def tDel(number):
    try:
        f = open('topics.txt', 'r')
        topics = f.readlines()
        f.close()
        if number >= len(topics):
            return [True, None]
        else:
            topics.remove(topics[number])
            f = open('topics.txt', 'w')
            f.write(''.join(topics))
            f.close()
            return [True, topics[number]]
        
    except Exception as error:
        return [False, 'Error in tDel: ' + str(error)]
