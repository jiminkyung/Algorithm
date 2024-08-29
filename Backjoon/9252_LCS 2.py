# 동적 계획법과 최단거리 역추적


# 참고 1👉 https://velog.io/@ledcost/%EB%B0%B1%EC%A4%80-9252-%ED%8C%8C%EC%9D%B4%EC%8D%AC-LCS-2-%EA%B3%A8%EB%93%9C-4-DP
# 참고 2(설명)👉 https://think-tech.tistory.com/55

# 메모리: 426796KB / 시간: 608ms
"""
- LCS[i][j] => S1의 i부터 S2의 j까지의 LCS값
- [i-1][j-1] 형식을 위해 각 문자열 앞에 빈 값을 추가해준다.
- S1과 S2의 문자 한글자씩 서로 비교.
  - 만약 S1[i] == S2[j]라면, 이전까지의 LCS값에 현재 문자를 추가한다.
  - 다르다면, LCS[i-1][j]와 LCS[i][j-1] 중 길이가 더 긴 값으로 저장한다.
    - [i-1][j]: S1의 현재 문자(i)를 제외한 이전까지의 결과
    - [i][j-1]: S2의 현재 문자(j)를 제외한 이전까지의 결과
"""

from sys import stdin


input = stdin.readline

S1 = [""] + list(input().rstrip())
S2 = [""] + list(input().rstrip())
LCS = [[""] * len(S2) for _ in range(len(S1))]

for i in range(1, len(S1)):
    for j in range(1, len(S2)):
        if S1[i] == S2[j]:
            LCS[i][j] = LCS[i-1][j-1] + S1[i]
        else:
            if len(LCS[i-1][j]) >= len(LCS[i][j-1]):
                LCS[i][j] = LCS[i-1][j]
            else:
                LCS[i][j] = LCS[i][j-1]

ret = LCS[-1][-1]
print(len(ret), ret, sep="\n")