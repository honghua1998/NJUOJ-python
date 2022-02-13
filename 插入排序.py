def Solution(l):
    for i in range(1,len(l)):
        key=l[i]
        j=i-1
        while j >=0 and l[j]>key:
            l[j+1]=l[j]
            j -=1
        l[j+1]=key
    return l

if __name__=="__main__":
    n=int(input())
    for _ in range(n):
        l=list(map(int,input().strip().split()))
        result=Solution(l[1:])
        print(" ".join(map(str,result)))