# 구현
# 정렬
# 두 포인터


# 문제: https://www.acmicpc.net/problem/1337

# 다른 풀이들을 보니, 보통은 "i부터 i+5까지 체크 -> 리스트에 존재하지 않는다면 +1" 방식으로 푸는듯?
# 풀이들이 다양한듯. 문제 분류가 두 포인터로 되어있는데, 다들 for문으로 푼 것 같다.
# 도움이 됐던 반례👉 https://www.acmicpc.net/board/view/126093

# 메모리: 32412KB / 시간: 36ms
from sys import stdin


input = stdin.readline

def main():
    N = int(input())
    
    arr = sorted(int(input()) for _ in range(N))
    # 두 수 사이의 차잇값 저장 (N-1개)
    new_arr = list(map(lambda x: x[1] - x[0] - 1, zip(arr, arr[1:])))

    min_cnt = 4

    for i in range(N-1):
        add = 0  # 추가해야 할 숫자 갯수
        cnt = 1  # 기존 배열에서 선택한 숫자 갯수
        for j in range(i, N-1):
            cnt += 1  # 배열에서 추가로 1개 더 선택
            add += new_arr[j]  # 선택한 숫자만큼 연속 배열로 만들기 위해 필요한 숫자 갯수
            if cnt + add <= 5:  # 만약 선택+추가한 숫자의 갯수가 5개 이하라면 최솟값 갱신
                min_cnt = min(add + (5 - (add + cnt)), min_cnt)
            else:  # 5개를 넘어가면 break 후 다음 턴으로
                break
    
    print(min_cnt)


main()