def minSwaps(arr,n):
    arr2=sorted(arr)
    count=0
    for i in range(n):
        if arr[i] == arr2[i]:
            i +=1
            continue

        else:
            k=arr.index(arr2[i])
            arr[i],arr[k] = arr[k],arr[i]
            count +=1
    print(count)

if __name__=="__main__":
    for _ in range(int(input())):
        n = int(input())
        arr1=list(map(int,input().strip().split(" ")))
        minSwaps(arr1,n)
