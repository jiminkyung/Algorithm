def solution(angle):
    if 0 < angle < 90:
        return 1
    elif angle == 90:
        return 2
    elif 90 < angle < 180:
        return 3
    else:
        return 4

# 이야~~~~ 대박이다! 나도 이렇게 머리쓰고싶다.
def solution(angle):
    answer = (angle // 90) * 2 + (angle % 90 > 0) * 1
    return answer

    # 1. 예각인 경우
    # (angle // 90) -> 0이므로 패스, (angle % 90 > 0) -> True니까 1, 1*1로 1 반환
    # 2. 직각인 경우
    # (angle // 90) -> 1이므로 1*2, (angle % 90 > 0) -> False이므로 패스. 즉 2 반환.
    # 3. 둔각인 경우
    # (angle // 90) -> 1이므로 1*2, (angle % 90 > 0) -> True니까 1, 2+1= 3 반환
    # 4. 평각인 경우
    # (angle // 90) -> 2이므로 2*2, 뒤에는 False이므로 패스. 4 반환

    # 멋있당