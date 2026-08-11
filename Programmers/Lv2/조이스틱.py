# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/42860


# 그리디로 분류되어 있어서 "현재 위치 -> 최적으로 이동할수있는 다음 위치" 방식으로 풀었으나 실패...
# "U턴은 최대 한번"이라는 키포인트를 생각하고 풀어야 함.
def solution(name: str) -> int:
    L = len(name)
    ret = 0

    # 문자 변환 횟수는 미리 계산해줌.
    for n in name:
        ret += min(ord(n) - 65, 91 - ord(n))
    
    min_move = L - 1

    for i in range(L):
        # "AAAAAA" 일경우 아래의 조건때문에 min_move = L - 1 이 되어버림.
        # if name[i] == "A":
        #     continue

        nxt = i + 1

        while nxt < L and name[nxt] == "A":
            nxt += 1
        
        # U턴은 최대 한번까지가 이득. 두번 이상부터는 손해다.
        # 현재 위치 i - 다음으로 A 이외의 문자가 나타나는 위치 nxt를 기점으로 왼쪽 U턴, 오른쪽 U턴을 계산해야함.
        # ex) BBAAAB 이고 i = 1 일경우,
            # 왼쪽 U턴: 0에서 왼쪽으로 i = 5까지 방문, 다시 0으로 되돌아와서 i = 1까지 방문.
            # 오른쪽 U턴: 0에서 오른쪽으로 i = 1까지 방문, 되돌아와서 왼쪽으로 i = 5까지 방문.

        # i 기준 왼쪽(-) 갔다가 오른쪽(+)
        left = 2 * (L - nxt) + i

        # 오른쪽(+) 갔다가 왼쪽(-)
        right = 2 * i + (L - nxt)

        min_move = min(min_move, left, right)

    return ret + min_move