# 구현
# 자료 구조
# 브루트포스 알고리즘
# 집합과 맵


# 문제: https://www.acmicpc.net/problem/2371
# 메모리: 32412KB / 시간: 40ms
from sys import stdin


input = stdin.readline

def main():
    N = int(input())
    files = []
    max_len = -1  # 최대 길이

    for _ in range(N):
        file = tuple(map(int, input().split()[:-1]))
        files.append(file)

        if max_len < len(file):
            max_len = len(file)

    # 앞자리부터 한자리씩 늘려가며 비교
    for K in range(1, max_len+1):
        # num = files[0][i] if len(files[0]) > i else 0
        """
        처음엔 위와 같이 작성했는데, 무작정 첫번째 값을 기준으로 비교할경우 다음과 같은 문제가 발생한다.
        입력:
        3
        1 -1
        1 2 -1
        1 2 3 -1
        
        정답은 3, 하지만 내 코드는 2를 출력한다. i=1일때 num은 0으로 할당되고,
        files[1][1]과 files[2][1]의 값은 2 이므로 curr_num != num을 만족해버리기 때문.
        실제로는 files[1][1] == files[2][1]이니 i=1일때 조건 불만족.
        """
        num = set()  # K개 선택한 값들
        for i in range(N):
            # 길이가 K보다 작으면 0 추가
            curr = files[i][:K] + tuple([0] * (K - len(files[i])))
            
            # 구별하지 못한다면 바로 break, 다음 K로 넘어감.
            if curr in num:
                break

            num.add(curr)
        
        # 모두 독립적인 상태라면 최소 K값 완성
        if len(num) == N:
            print(K)
            break


main()