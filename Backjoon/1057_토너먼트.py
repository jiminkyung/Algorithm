# 문제집 - 0x12강 - 수학


# 문제: https://www.acmicpc.net/problem/1057
# 메모리: 32412KB / 시간: 36ms
N, kim, lim = map(int, input().split())

round = 0

while kim != lim:  # 같은 조가 되면 break
    kim = (kim + 1) // 2
    lim = (lim + 1) // 2
    round += 1

print(round)