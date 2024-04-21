"""
yellow 길이 = (전체길이 - 2)
brown 길이 = 전체길이
다시말해, yellow의 가로세로를 x, y라고 한다면,
-> (x+2)(y+2) = brown + yellow
-> yellow = xy
-> 2x + 2y + 4 = brown 가 된다.

- TC 11, 12에서 실패함 => 반복문 범위를 1부터 잡아야한다.
"""

def solution(brown, yellow):
    for i in range(1, int(yellow**0.5)+1):
        if yellow % i == 0:
            x, y = max(i, yellow//i), min(i, yellow//i) # 가로=세로 or 가로>세로 여야함.
            if (x*2 + y*2 + 4) == brown:
                return [x+2, y+2]