# 비트마스킹


# 문제: https://www.acmicpc.net/problem/1322

# 비트마스킹 연습하기 좋은 문제!
# 메모리: 32412KB / 시간: 40ms
from sys import stdin


input = stdin.readline

def main():
    # 조건: X + Y == X | Y
    # 즉, X & Y == 0 이어야함.
    # 겹치는 비트가 있으면 안됨.
    X, K = map(int, input().split())

    zero = []
    tmp = X
    pos = 0

    # X를 이진수로 변환했을때 0이 위치한 인덱스를 zero에 저장함
    while tmp:
        if tmp & 1 == 0:
            zero.append(pos)
        pos += 1
        tmp >>= 1
    
    """
    X의 0비트 자리에만 Y가 비트를 세울 수 있음. X & Y == 0 이어야하니까.
    그런데 만약, X의 0비트 개수만으로는 K번째 조합을 만들 수 없다면?
    -> X보다 큰 자리(상위 비트)까지 확장해서 새로운 0자리를 만들어야함.

    🗝️ 여기서 왜 K를 비트로 쪼개는 거냐?
    수의 증가 순서를 보면 1, 10, 11, 100, 101, 110, 111...
    이런 식으로 진행되므로, 이진수 자체가 조합의 순서를 정확히 알려주는 셈.

    예를 들어 K = 6이면, 이진수로는 110가 됨.
    -> 우리가 만들어야 할 Y는, 0비트 자리 중에서
        - zero[1] 위치에 1 넣고
        - zero[2] 위치에도 1 넣은 조합이라는 뜻!

    그래서 zero 리스트를 만들어서,
    -> zero[0] = X에서 오른쪽에서부터 첫 번째 0비트 위치
    -> zero[1] = 두 번째 0비트 위치
    이런 식으로 인덱싱해서, Y를 만들 때 참고할 수 있게끔 할 거임.
    """

    # 2. 만약 0의 갯수로 만들 수 있는 조합이 K보다 작다면, K개를 만족할때까지 X앞에 새로운 비트자리를 추가.
    while len(zero) < K.bit_length():
        zero.append(pos)
        pos += 1

    ret = 0
    
    # 이진수 K의 오른쪽에서 i번째에 위치하는 비트
    # 만약 1이라면? zero[i]번째 비트를 1로 켜줌.
    for i in range(len(zero)):
        if (K >> i) & 1 == 1:
            ret |= (1 << zero[i])
    
    print(ret)


main()