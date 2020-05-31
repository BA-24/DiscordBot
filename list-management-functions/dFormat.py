#formats topics and notes to a discord friendly list

def dFormat():
    try:
        printlist = []
        for x in range(tLen()[1]):
            topic = tGet(x)
            if topic[0] == True and topic[1] != None:
                printlist = printlist + [(str(x + 1) + '. **' + topic[1] + '**\n')]

                note = nGet(x, False)
                if note[0] == True and note[1] != None:
                    printlist = printlist + [ ( '*' + note[1] + '*\n' ) ]
        return [True, "".join(printlist)]
    except Exception as error:
        return [False, error]
