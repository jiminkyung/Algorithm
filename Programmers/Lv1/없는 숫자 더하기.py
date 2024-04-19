def solution(numbers):
    nums = set(range(1, 10))
    ret = nums - set(numbers)
    return sum(ret)