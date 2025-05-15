# 구현
# 브루트포스 알고리즘


# 문제: https://www.acmicpc.net/problem/1195

# 재미있는 문제다~ 다시 풀어봐도 좋을 듯.
# 메모리: 32412KB / 시간: 44ms
from sys import stdin


input = stdin.readline

def main():
    g1 = input().rstrip()
    g2 = input().rstrip()

    min_len = len(g1) + len(g2)
    """
    -4-3-2-1 01 2 3 4 5 6 7 8 9 10  (인덱스)
    ㅁㅁㅁㅁㅁ          ㅁㅁㅁㅁㅁ  <- g2
            ㅁㅁㅁㅁㅁㅁㅁ          <- g1
    g1을 고정시키고 g2를 g1의 왼쪽 ~ 오른쪽으로 움직여본다.
    위 그림처럼 왼쪽 - 오른쪽 모두를 포함한 길이를 전체 범위라고 생각했을때,
    g2의 0 인덱스가 올 수 있는 전체 인덱스는 -len(g2)+1 ~ len(g1)-1 이다.
    - 기어가 겹쳐야하므로 g2와 g1이 최소 한 칸은 겹쳐져있다고 가정.
    - 초기 min_len은 겹치는 구간이 아예 없을때를 가정한 값.
    
    해당 인덱스로 g1의 인덱스를 구한다. => g1 = i + g2전체인덱스
    예를들어 g2 길이가 5, g1 길이가 7 이라면 가능한 g2[0]의 범위는 -4 ~ 6가 된다.
    만약 g2인덱스를 -2로 설정했다면,
    - g1 = i + (-2)
    계산한 g1인덱스값이 0 ~ len(g1)-1 범위 내에 존재할경우 맞물리는지 확인한다.
    """

    def check(g1, g2, idx2):
        for i in range(len(g2)):
            j = i + idx2
            if 0 <= j < len(g1):
                if g1[j] == "2" and g2[i] == "2":
                    return False
        return True
    

    for idx2 in range(-len(g2)+1, len(g1)):
        # 만약 g1과 g2가 완벽하게 맞물린다면 최소 길이 갱신
        if check(g1, g2, idx2):
            left = min(0, idx2)  # (g1이 g2보다 왼쪽에 있는 경우, g2가 g1보다 왼쪽에 있는 경우)
            right = max(len(g1), idx2 + len(g2))  # (g2가 g1보다 왼쪽에 있는 경우, g1이 g2보다 왼쪽에 있는 경우)
            # 인덱스는 0부터 시작하므로 idx2 + len(g2)는 실제 g2의 끝 인덱스값보다 +1 인 상태다.
            # 따라서 전체 길이를 구할 때 그냥 right - left 로 계산 가능.
            length = right - left
            min_len = min(length, min_len)
    
    print(min_len)


main()