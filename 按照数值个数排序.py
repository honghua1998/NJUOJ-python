from collections import defaultdict
if __name__=="__main__":
    case_num=int(input().strip())
    for i in range(case_num):
        _=input()
        arr=[int(x) for x in input().strip().split((" "))]
        dict = defaultdict(int)
        for x in arr:
            dict[x] +=1
        dict2=sorted(dict.items(),key=lambda x:(-x[1],x[0]))
        res=[]
        for k,v in dict2:
            for i in range(v):
                res.append(str(k))
        print(" ".join(res))