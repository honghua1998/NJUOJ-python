def find4Numbers(A, n, k):
    A.sort()
    quadruplets = list()
    if not A or len(A) < 4:
        return quadruplets
    for i in range(n-3):
        if i > 0 and A[i] == A[i-1]:
            continue
        if A[i] + A[i+1] + A[i+2] + A[i+3] > k:
            break
        if A[i] + A[n-3] + A[n-2] + A[n-1] < k:
            continue
        for j in range(i+1, n-2):
            if j > i + 1 and A[j] == A[j-1]:
                continue
            if A[i] + A[j] + A[j+1] + A[j+2] > k:
                break
            if A[i] + A[j] + A[n-2] + A[n-1] < k:
                continue
            l = j + 1
            r = n - 1
            while l < r:
                total = A[i] + A[j] + A[l] + A[r]
                if total == k:
                    quadruplets.append([A[i], A[j], A[l], A[r]])
                    print(A[i],A[j],A[l],A[r],'',sep=" ",end="$")
                    while l < r and A[l] == A[l+1]:
                        l = l + 1
                    l = l + 1
                    while l < r and A[r] == A[r-1]:
                        r = r -1
                    r = r -1
                elif total < k:
                    l = l + 1
                else:
                    r = r - 1
    return quadruplets
if __name__ == "__main__":
    for _ in range(int(input())):
        n_k = list(map(int, input().strip().split(" ")))
        A = list(map(int, input().strip().split(" ")))
        n = n_k[0]
        k = n_k[1]
        find4Numbers(A,n,k)
        print('\r')
# 输出还是有点问题
# 输出还是有点问题
# A = [10,2,3,4,5,7,8]
# n=7
# k=23
# find4Numbers(A,n,k)
# A = [2,2,2,2,2,2,2,2,2,2]
# n = 10
# k = 8
# find4Numbers(A,n,k)


"""
2
5 3
0 0 2 1 1 
7 23
10 2 3 4 5 7 8

0 0 1 2 $
2 3 8 10 $2 4 7 10 $3 5 7 8 $
"""

"""
class Solution:
    def fourSum(self, nums, target):
        quadruplets = list()
        if not nums or len(nums) < 4:
            return quadruplets

        nums.sort()
        length = len(nums)
        for i in range(length - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            if nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:
                break
            if nums[i] + nums[length - 3] + nums[length - 2] + nums[length - 1] < target:
                continue
            for j in range(i + 1, length - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                if nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target:
                    break
                if nums[i] + nums[j] + nums[length - 2] + nums[length - 1] < target:
                    continue
                left, right = j + 1, length - 1
                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]
                    if total == target:
                        quadruplets.append([nums[i], nums[j], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        right -= 1
                    elif total < target:
                        left += 1
                    else:
                        right -= 1

        return quadruplets

solution = Solution()
nums = [2,2,2,2,2,2,2,2,2,2]
target = 8
print(solution.fourSum(nums,target))"""