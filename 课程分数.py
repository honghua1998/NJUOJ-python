class Marks(object):
    def __init__(self, py=0, ch=0, ma=0):
        self.py = py
        self.ch = ch
        self.ma = ma

    def printdetails(self):
        print(str(self.py) + ' ' + str(self.ch)+' '+str(self.ma))


def getinput():
    allmarks = []
    for _ in range(int(input())):
        batchmarks = []
        for _ in range(int(input())):
            newobj = Marks()
            newobj.py, newobj.ch, newobj.ma = list(map(int, input().strip().split(" ")))
            batchmarks.append(newobj)
            allmarks.append(newobj)
    return allmarks

def pymarksAsc(markslist):
    # 按照物理成绩排序
    for i in range(1,len(markslist)):
        for j in range(0,len(markslist)-i):
            if markslist[j].py > markslist[j+1].py:
                markslist[j],markslist[j+1] = markslist[j+1],markslist[j]
    return markslist

def chmarksDes(markslist):
    for i in range(1,len(markslist)):
        for j in range(0,len(markslist)-i):
            if markslist[j].py == markslist[j+1].py:
                if markslist[j].ch < markslist[j+1].ch:
                    markslist[j],markslist[j+1] = markslist[j+1],markslist[j]
    return markslist

def mamarksAsc(markslist):
    for i in range(1,len(markslist)):
        for j in range(0,len(markslist)-i):
            if (markslist[j].py == markslist[j+1].py) & (markslist[j].ch == markslist[j+1].ch):
                if markslist[j].ma > markslist[j+1].ma:
                    markslist[j], markslist[j + 1] = markslist[j + 1], markslist[j]
    return markslist

def printmarks(markslist):
    for item in markslist:
        item.printdetails()

if __name__ == "__main__":
    printmarks(mamarksAsc(chmarksDes(pymarksAsc(getinput()))))