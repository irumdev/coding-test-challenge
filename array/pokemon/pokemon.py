def solution(nums):
    cont = len(nums) / 2
    nums = set(nums)

    return min(len(nums), cont)
