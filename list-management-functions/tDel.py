def tDel(number):
    try:
        f = open('topics.txt', 'r')
        topics = f.readlines()
        f.close()
        if number >= len(topics):
            return [True, None]
        else:
            removed = topics[number]
            topics.remove(removed)
            f = open('topics.txt', 'w')
            f.write(''.join(topics))
            f.close()
            return [True, removed]
        
    except Exception as error:
        return [False, 'Error in tDel: ' + str(error)]
