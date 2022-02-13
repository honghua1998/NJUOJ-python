def get_requied_students(arr,cap):
    nunOfStudents = 1
    sum = 0
    for x in arr:
        sum += x
        if sum > cap:
            nunOfStudents += 1
            sum = x
    return nunOfStudents

def solution(i, j, arr, k):
    if i == j:
        print(i)
        return
    mid = (i+j) >> 1
    p_num = get_requied_students(arr,mid)
    if p_num <= k:
        solution(i, mid, arr, k)
    else:
        solution(mid+1, j, arr, k)


if __name__ == '__main__':
    for _ in range(int(input())):
        _ = int(input())
        arr = list(map(int,input().strip().split(" ")))
        k = list(map(int,input().strip().split(" ")))[0]
        min_cap = max(arr)
        max_cap = sum(arr)
        if k > len(arr):
            print(-1)
        else:
            solution(min_cap, max_cap, arr, k)