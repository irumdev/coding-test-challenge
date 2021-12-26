def solution(nums):
    cont = len(nums) / 2
    nums = set(nums)

    return cont if len(nums) >= cont else len(nums)
