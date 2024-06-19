# 집합과 맵
# 메모리: 240712KB / 시간: 516ms

from sys import stdin


S = stdin.readline()

ret = set()

for i in range(len(S)):
    for j in range(i+1, len(S)):
        ret.add(S[i:j])

print(len(ret))


# 숏코딩. 문자열의 최대 길이가 1000이기 때문에 t를 1001으로 설정한듯.
s=input()
t=1001
print(len({s[i%t:i//t]for i in range(t*t)})-1)