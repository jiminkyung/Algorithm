def solution(nums):
    n = len(nums) // 2
    sets = list(set(nums))
    return n if len(sets) >= n else len(sets)