# def mergeKArrays(arr,k,output):
#     c = 0
#     for i in range(k):
#         for j in range(k):
#             output[c] == arr[i][j]
#             c += 1
#     output.sort()
#     return output

def printArray(arr,k):
    print(" ".join(str(arr[i]) for i in range(k**2) ))
    # for i in range(k**2):
    #     print(arr[i],end=" ")
    # print("\r")



if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        arr = list(map(int,input().strip().split(" ")))
        arr.sort()
        printArray(arr,n)


