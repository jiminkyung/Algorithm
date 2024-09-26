# 기하 2


# 문제: https://www.acmicpc.net/problem/7869
# 일단 참고... https://wondangcom.tistory.com/1900
from sys import stdin
import math


input = stdin.readline

x1, y1, r1, x2, y2, r2 = map(float, input().split())
dis = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

if r1 + r2 < dis:
    ret = 0.0
elif abs(r1 - r2) >= dis:
    ret = min(r1, r2) ** 2 * math.pi
else:
    # 원1, 원2의 부채꼴 넓이의 합 - 원1, 원2의 삼각형 넓이의 합
    theta1 = math.acos((r1**2 + dis**2 - r2**2) / (2 * r1 * dis))  # 원1의 중심각
    theta2 = math.acos((r2**2 + dis**2 - r1**2) / (2 * r2 * dis))  # 원2의 중심각

    # 부채꼴의 넓이 합 구하기
    area = r1**2*theta1 + r2**2*theta2
    # 삼각형 넓이 합
    h = r1 * math.sin(theta1)  # 삼각형의 높이
    b = r1 * math.cos(theta1)  # 삼각형의 밑변
    triangle = h * b  # 어차피 2개이므로 /2는 pass

    ret = area - triangle

print(f"{ret:.3f}")

# 위 방법은 틀리다함~ 이유가 뭘까...?^^
# 참고하자 => https://lighter.tistory.com/136
# 왠진 모르겠지만... 맞다는 방식으로 다시 작성해보자.

# 메모리: 33240KB / 시간: 32ms
from sys import stdin
import math


input = stdin.readline

x1, y1, r1, x2, y2, r2 = map(float, input().split())
dis = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

if r1 + r2 < dis:
    ret = 0.0
elif abs(r1 - r2) >= dis:
    ret = min(r1, r2) ** 2 * math.pi
else:
    # 원1, 원2의 부채꼴 넓이의 합 - 원1, 원2의 삼각형 넓이의 합
    theta1 = 2 * math.acos((r1**2 + dis**2 - r2**2) / (2 * r1 * dis))  # 원1의 중심각
    theta2 = 2 * math.acos((r2**2 + dis**2 - r1**2) / (2 * r2 * dis))  # 원2의 중심각

    # 각 원의 교차지점 넓이
    area1 = r1 ** 2 * (theta1 - math.sin(theta1)) / 2
    area2 = r2 ** 2 * (theta2 - math.sin(theta2)) / 2

    ret = area1 + area2

print(f"{ret:.3f}")

# 여러가지 방법을 시도해봤으나 위 방법 외엔 정확한 값을 얻을 수 없었다.
# r1, r2와 theta를 이용해 높이 x 밑변으로 삼각형의 넓이를 구하는건, 곡률이 고려되지 않아 정확한 답을 얻을 수 없단다.