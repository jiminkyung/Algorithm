# 기하 2


# 문제: https://www.acmicpc.net/problem/11758
# 벡터의 외적, CCW 관련 좋은 설명! 참고👉 https://degurii.tistory.com/47

# 메모리: 31120KB / 시간: 40ms
from sys import stdin


input = stdin.readline

coordinate = [tuple(map(int, input().split())) for _ in range(3)]

AB = (coordinate[1][0]-coordinate[0][0], coordinate[1][1]-coordinate[0][1])
AC = (coordinate[2][0]-coordinate[0][0], coordinate[2][1]-coordinate[0][1])

ret = AB[0] * AC[1] - AB[1] * AC[0]

if ret > 0:
    print(1)
elif ret < 0:
    print(-1)
else:
    print(0)


# 마지막 ret 표현부분을 한줄로 변경한 버전.
# 메모리: 31252KB / 시간: 36ms
from sys import stdin


input = stdin.readline

coordinate = [tuple(map(int, input().split())) for _ in range(3)]

AB = (coordinate[1][0]-coordinate[0][0], coordinate[1][1]-coordinate[0][1])
AC = (coordinate[2][0]-coordinate[0][0], coordinate[2][1]-coordinate[0][1])

ret = AB[0] * AC[1] - AB[1] * AC[0]

print(1 if ret > 0 else -1 if ret < 0 else 0)
# 삼항 연산자를 사용 시 임시 객체가 생성되기 때문에, 조건에 부합하면 바로 결과를 출력해주는 단순 if-else문과 메모리 차이가 난다.