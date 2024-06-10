# 브루스포트 방식으로 푼 코드. 사실 브루스포트 항목 문제이기때문에 정석 답안은 이게 맞다.
# 메모리: 31120KB / 시간: 104ms
N, M = map(int, input().split())
cards = list(map(int, input().split()))

ret = 0
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            total = cards[i] + cards[j] + cards[k]
            
            if total <= M:
                ret = max(ret, total)

print(ret)


# 투 포인터 알고리즘 사용
# 시간: 104ms. 시간이 훨씬 줄어들었다.
N, M = map(int, input().split())
cards = list(map(int, input().split()))

cards.sort()

ret = 0
for i in range(N - 2):
    left = i + 1
    right = N - 1
    while left < right:
        total = cards[i] + cards[left] + cards[right]
        if total <= M:
            ret = max(ret, total)
            left += 1
        else:
            right -= 1

print(ret)