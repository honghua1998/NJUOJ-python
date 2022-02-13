"""
main函数用来接受并处理用户输入，调用函数，处理异常以及排版输出，
quicks-sort用来进行一次快排，返回一次快排后的数组以及left
solution就是解决方案，输入的参数为l，是经过main处理好的输入，
    具体的非递归逻辑就在这里
        用栈可以很好的模拟递归，一次压入两个，pop两个，
"""
def solution(l):
    stack = []
    stack.append(len(l)-1)
    stack.append(0)
    while len(stack) != 0:
        left=stack.pop()
        right = stack.pop()
        l,key = quick_sort(l,left,right)
        if left < key -1:
            stack.append(key -1)
            stack.append(left)

        if right > key +1:
            stack.append(right)
            stack.append(key +1)

    return l

def quick_sort(l,left,right):
    temp = l[left]
    while left < right:
        while left <right and l[right]>=temp:
            right -=1
        l[left]=l[right]
        while left < right and l[left] <=temp:
            left +=1
        l[right]=l[left]
    l[left]=temp
    return l,left

if __name__ =="__main__":
    while True:
        try:
            l=list(map(int,input().strip().split()))
            if len(l) == 0:
                break

            result = solution(l[1:])
            print(" ".join(map(str,result)))
        except EOFError:
            break