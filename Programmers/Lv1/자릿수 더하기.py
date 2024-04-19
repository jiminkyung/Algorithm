def solution(n):
    return sum(list(map(int, (str(n)))))

# 재귀로 푸신 분 코드. 멋있다.
def sum_digit(number):
    if number < 10:
        return number
    return number%10 + sum_digit(number//10)