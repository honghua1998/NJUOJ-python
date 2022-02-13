def solution(l):
    i = 1
    while i < len(l):
        low = 0
        while low < len(l):
            mid = low + i
            high = min(len(l), mid + i)
            if mid < high:
                l = merge_sort(l, low, mid, high)
            low += 2 * i
        i = i * 2
    return l


def merge_sort(l, low, mid, high):
    l1 = l[low: mid]
    l2 = l[mid: high]
    i = 0
    j = 0
    res = []
    while i < len(l1) and j < len(l2):
        if l1[i] <= l2[j]:
            res.append(l1[i])
            i += 1
        elif l1[i] > l2[j]:
            res.append(l2[j])
            j += 1
    if i != len(l1):
        res += l1[i:]
    if j != len(l2):
        res += l2[j:]
    l[low: high] = res
    return l


if __name__ == '__main__':
    while True:
        try:
            l = list(map(int, input().strip().split()))
            if len(l) == 0:
                break
            result = solution(l[1:])
            print(" ".join(map(str, result)))
        except EOFError:
            break
