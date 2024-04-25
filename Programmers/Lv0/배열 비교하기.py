def solution(arr1, arr2):
    if len(arr1) == len(arr2):
        if sum(arr1) > sum(arr2):
            return 1
        elif sum(arr1) < sum(arr2):
            return -1
        else:
            return 0
    else:
        if len(arr1) > len(arr2):
            return 1
        else:
            return -1

# 우왕
def solution(arr1, arr2):
    return (len(arr1) > len(arr2)) - (len(arr2) > len(arr1)) or (sum(arr1) > sum(arr2)) - (sum(arr2) > sum(arr1))

# 다른분 코드 보고 신기해서 테스트 해본 코드.
test1 = [1, 2]
test2 = [1, 2, 3]
(len(test1) > len(test2)) + (len(test1) < len(test2))