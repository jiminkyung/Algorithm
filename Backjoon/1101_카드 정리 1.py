# 그리디 알고리즘


# 문제: https://www.acmicpc.net/problem/1101

# 2차원 배열 고대로 브루트포스로 풀면 시간초과날듯 ㅜㅜ
# 참고: https://popcorn-overflow.tistory.com/4

# 메모리: 32412KB / 시간: 40ms
from sys import stdin


input = stdin.readline

def main():
    """
    원리는 이러함.
    안 옮겨도 되는 박스들을 제외하고 모두 조커박스로 옮겨주는거임.

    각 박스들을 탐색한다. 그럼 아래와 같은 경우로 나뉘게 됨.
    - 빈 박스
    - 여러 카드가 섞인 박스
    - 한 종류의 카드만 있는 박스

    한 종류만 있다면, 해당 카드번호를 one에 저장한다.
    여러 카드가 섞여있다면, jocker에 저장한다.

    다 처리했다면 set(one)으로 중복되는 카드번호를 제거한다.
    즉,
    one의 값 = 한 종류의 카드만 나타났을때의 카드번호
    set(one)의 값 = 카드가 여러 군데 나뉘어있는 경우를 제외시킨 경우
    그럼 len(one) - len(set(one))은,
    => 여러 군데 나뉘어져있는 카드들을 조건에 맞춰 한 곳으로 몰아넣는 경우

    만약 모든 카드가 한 박스가 아닌 여러 박스에 나뉘어져 있는 상태라면?
    경우의 수는 커질것이다.
    반대로 0개, 혹은 몇 개의 카드번호만 나뉘어져있다면 작아지겠지.

    그리고 여기서 jocker의 길이를 체크해준다.

    만약 jocker박스가 하나도 없다면, 모두 빈 박스 or 한 박스에 한개의 카드만 존재 하는경우다.
    그렇다면, one의 박스 중 아무 박스나 조커 박스로 지정해준다면 그 박스의 카드들은 옮기지 않아도 됨.
    따라서 len(one) - len(set(one))를 cnt로 했을때, cnt가 1 이상일경우 cnt-1이 답이 되겠다.
    
    jocker박스가 존재한다면, 그 중 하나를 리얼 조커박스로 선택하는거다. => len(jocker)-1
    여기다 cnt를 더해주면 총 몇번 옮겨야하는지 구할 수 있다.
    선택한 조커 박스 외의 박스들을 옮기는 경우 => len(jocker) - 1
    한 박스에 하나의 카드 or 빈 박스가 되도록 옮기는 경우 => len(one) - len(set(one))

    두뇌단련만이 살 길이다.
    """
    N, M = map(int, input().split())
    boxes = [list(map(int, input().split())) for _ in range(N)]

    one = []
    jocker = []

    for box in boxes:
        idx = -1

        for card in range(M):
            if box[card] != 0:
                if idx != -1:
                    jocker.append(box)
                    break
                idx = card
        else:
            if idx != -1:
                one.append(idx)
    
    tmp = set(one)
    
    # one: 박스에 한 색상만 존재하는 경우, tmp: one의 경우들을 set으로 변환.
    # => 여러군데 나뉘어있는 색상들은 한곳으로 모아야하므로, 나뉘어진 경우만큼 이동시켜야함.
    cnt = len(one) - len(tmp)

    # 걍 조커박스 + cnt > 0 이면 -1 해주고, 아니면 그대로 출력해주면 될듯.
    # cnt = len(one) - len(tmp) + len(jocker)
    # print(cnt-1 if cnt > 0 else cnt)
    # 위 방식대로 해도 정답임.

    if len(jocker) == 0:
        print(cnt - int(cnt > 0))
    else:
        # len(jocker)-1: 박스 중 한곳을 조커박스로 지정
        print(len(jocker)-1 + cnt)


main()