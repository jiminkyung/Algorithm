def solution(numbers, k):
    length = len(numbers)
    index = (k - 1) * 2 % length
    return numbers[index]

# 런타임 오류가 나서 AI돌렸다. danny한테 위스키 추천이나 받아야겠다...ㅎ