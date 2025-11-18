# 구현
# 브루트포스 알고리즘
# 시뮬레이션
# 누적 합


# 문제: https://www.acmicpc.net/problem/2811

# 생각보다 잔 오류가 있었던 문제.
# 나중에 구현 연습할때 다시 풀어볼만한듯.

# 메모리: 41144KB / 시간: 64ms
from sys import stdin


input = stdin.readline

def main():
    N = int(input())
    days = list(map(int, input().split()))

    # 스즈미야 상범이의 우울

    # 모든 우울기간을 (우울기간, 시작일, 종료일) 형태로 저장
    candidates = []
    total = [0] * N  # total[i]: i날에 꽃을 주는지 여부
    cnt = 0
    start = -1

    for i in range(N):
        # 만약 우울한날이라면 우울기간 카운트
        if days[i] < 0:
            cnt += 1
            if start == -1:  # 우울기간 첫 날이라면 시작일 저장
                start = i
        else:
            # 우울기간이 끝났다면 꽃을 줘야 하는 날들을 갱신한다. (2T)
            if cnt > 0:
                for j in range(max(0, start - 2*cnt), start):
                    total[j] = 1
                # 우울기간 후보군에 추가
                candidates.append((cnt, start, i-1))
                start = -1
                cnt = 0
    else:
        # 마지막날까지 우울했다면 우울기간 처리가 안 된 상황이므로, 따로 처리해줌.
        if cnt > 0:
            for j in range(max(0, start - 2*cnt), start):
                total[j] = 1
            candidates.append((cnt, start, i-1))
    
    # 1순위 조건은 "우울기간의 길이"이므로, 우울 기간을 기준으로 내림차순으로 정렬.
    candidates.sort(reverse=True)

    # max_cand = (우울기간, 3T로 가정 시 추가로 꽃을 줘야하는 날들, 시작일, 종료일)
    max_cand = (0, 0, 0, 0)
    for cnt, s, e in candidates:
        # 현재 우울기간이 최대 우울 기간보다 짧다면 종료
        if cnt < max_cand[0]:
            break
        # 시작일과 3T 전날 사이의 일수
        size = s - max(0, s - 3*cnt)
        # 3T로 계산했을때의 일수에서 sum(total[max(0, s-3*cnt):s])을 뺀다.
        # 3T를 어느 날로 잡느냐와는 상관없이 무조건 꽃을 줘야하는 날들, 즉 기존에 2T 기준으로 계산했던 날들을 빼주는것.
        # 그럼 val_days = 기존의 꽃을 줘야 하는 날들을 제외하고, 현재 기간을 최대 우울기간으로 잡았을때 새롭게 꽃을 줘야하는 날들이 된다.
        val_days = size - sum(total[max(0, s-3*cnt):s])
        # 이 값이 이전 최댓값보다 크다면 변경!
        if cnt > max_cand[0] or (cnt == max_cand[0] and val_days > max_cand[1]):
            max_cand = (cnt, val_days, s, e)
    
    # 최종적인 최대 우울기간을 total에 반영
    start = max(0, max_cand[2] - 3*max_cand[0])
    for i in range(start, max_cand[2]):
        total[i] = 1
    
    print(sum(total))


main()