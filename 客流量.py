"""
2
5
1 2 10 5 5
4 5 12 9 12
7
13 28 29 14 40 17 3
107 95 111 105 70 127 74
"""
def getinput():
    allguest = []
    for _ in range(int(input())):
        numofguests = int(input())
        entrylist = list(map(int, input().strip().split(" ")))
        outlist = list(map(int, input().strip().split(" ")))
        guest = []
        for i in range(numofguests):
            guest.append(list(range(entrylist[i], outlist[i]+1)))
        allguest.append(guest)
    return allguest

def getrange(allguset):
    """
    [[1, 2, 3,.., 12], [3, 4, 5,.., 127]]
    :param allguset:
    :return:
    """
    guestrange = []
    for i in range(len(allguset)):
        tempmin = allguset[i][0][0]
        tempmax = allguset[i][0][-1]
        for j in range(len(allguset[i])):
            left = allguset[i][j][0]
            right = allguset[i][j][-1]
            if left < tempmin:
                tempmin = left
            if right > tempmax:
                tempmax = right
        guestrange.append(list(range(tempmin, tempmax+1)))

    return guestrange

def getresult():
    """
    3 5
    7 40
    :return:
    """
    originlist = getinput()

    contrastlist = getrange(originlist)
    for i in range(len(contrastlist)):
        count = [0] * len(contrastlist[i]) * 2
        for j in range(len(contrastlist[i])):
            for k in range(len(originlist[i])):
                if contrastlist[i][j] in originlist[i][k]:
                    count[j] = count[j] + 1
        countmax = max(count)
        maxindex = count.index(countmax) + contrastlist[i][0]
        print(str(countmax)+" "+str(maxindex))


    return

if __name__ == "__main__":
    getresult()











