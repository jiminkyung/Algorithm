def solution(numbers, n):
    result = 0
    for num in numbers:
        if result <= n:
            result += num
    return result