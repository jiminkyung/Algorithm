def solution(arr):
    binary = bin(len(arr))
    if '1' in binary[3:]:
        s = '0b1' + '0' * len(binary[2:])
    else:
        return arr
    return arr + [0] * (int(s, 2) - int(binary, 2))

# 다른분이 시간복잡도에 대해 설명한건데, 나중에 찾아보자
def solution(arr):
    a = 1
    b = len(arr)
    while a < b :
        a *= 2
    return arr + [0] * (a-b)

"""
2의 거듭제곱 확인 방법 O(1)로 해야 겨우 O(n)
logn으로 확인하면 그걸 n번 반복 -> o(nlogn)
길이 1000개 -> 가장 빠른방법은 각각 하드코딩하기 겨우 10개
"""