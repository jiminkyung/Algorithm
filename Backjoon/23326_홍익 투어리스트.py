# 문제집 - 0x16강 - 이진 검색 트리


# 문제: https://www.acmicpc.net/problem/23326

# 이진 탐색만 사용하면 통과 X
# 세그먼트 트리를 사용해야 통과할 수 있음.

# 참고한 풀이👉 https://www.acmicpc.net/source/55886239
# 메모리: 53528KB / 시간: 2248ms
from sys import stdin


input = stdin.readline

N, Q = map(int, input().split())
A = list(map(int, input().split()))
landmark = sum(A)  # 명소의 갯수

# 명소 업데이트(세그먼트 트리 업데이트) 함수
def update(target, node, left, right):
    # 현재 노드 값 업데이트
    seqt[node] += P  # P: target을 명소로 추가한다면 1, 명소리스트에서 삭제한다면 -1

    if left == right:
        return

    mid = (left + right) // 2

    if target <= mid:  # 찾는 명소가 mid보다 작거나 같다면 왼쪽 서브트리로
        update(target, 2*node, left, mid)
    else:  # mid보다 크다면 오른쪽 서브트리로
        update(target, 2*node + 1, mid+1, right)


# 현재 위치까지의 명소의 갯수를 카운트하는 함수 (현재 위치 포함)
def count_landmark(node, left, right):
    global cnt

    if left == right:
        return
    
    mid = (left + right) // 2

    if curr <= mid:  # 현재 위치가 mid보다 작거나 같다면 왼쪽 서브트리로
        count_landmark(2*node, left, mid)
    else:  # mid보다 크다면 왼쪽 서브트리값을 cnt에 추가, 오른쪽 서브트리로 이동
        cnt += seqt[2*node]
        count_landmark(2*node + 1, mid+1, right)


# 다음 명소의 위치를 찾는 함수
def find_landmark(node, left, right):
    global cnt, ret

    if left == right:
        ret = left
        return
    
    mid = (left + right) // 2

    if cnt <= seqt[2*node]:  # cnt값이 왼쪽 서브트리의 값보다 작거나 같다면, 왼쪽 서브트리로 이동
        find_landmark(2*node, left, mid)
    else:  # 왼쪽 서브트리보다 크다면, 왼쪽 서브트리의 값을 빼고 오른쪽 서브트리로 이동
        cnt -= seqt[2*node]
        find_landmark(2*node + 1, mid+1, right)


# 세그먼트 트리 생성
seqt = [0] * (4*N)

# 기존 명소들을 세그먼트 트리에 저장
for i in range(N):
    if A[i]:
        P = 1
        update(i+1, 1, 1, N)

# 현재 위치: 1-based로 관리함
curr = 1

# 쿼리문 실행
for _ in range(Q):
    cmd, *x = map(int, input().split())

    # 1: 명소 toggle
    if cmd == 1:
        target = x[0]
        
        # 이미 명소로 지정된 장소라면 제거
        if A[target-1]:
            A[target-1] = 0
            landmark -= 1
            P = -1  # 제거해줘야 하므로 -1로 설정
        else:
            A[target-1] = 1
            landmark += 1
            P = +1
        update(target, 1, 1, N)

    # 2: 인간 이동
    elif cmd == 2:
        dis = x[0]

        curr = ((curr - 1 + dis) % N) + 1  # 현재 위치에서 dis만큼 이동
    
    else:
        # 명소가 아예 없다면 -1 출력 후 넘어감
        if not seqt[1]:
            print(-1)
            continue

        cnt = 1  # 현재 위치 이후의 cnt번째 명소
        count_landmark(1, 1, N)
        
        # 만약 카운팅 한 결과값이 실제 명소의 갯수+1 일경우 -> curr 이후 명소 X, 첫번째 명소가 제일 가까운 셈
        if cnt == landmark+1:
            cnt = 1
        
        ret = 0
        find_landmark(1, 1, N)
        print((ret - curr) % N)