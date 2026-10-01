# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/60059


# 구현 연습하기 좋은 문제
# 자물쇠의 홈들 중 하나를 기준으로 잡고, 키 맵을 변화시켜가며 검사함.
# 아니면 자물쇠 맵에 키 맵 크기만큼 상하좌우로 여백을 추가하고, 열쇠를 모든 위치에 대입해도 될듯?ㄴ
def solution(key: list[list[int]], lock: list[list[int]]) -> bool:
    M, N = len(key), len(lock)

    x = y = -1  # 제일 먼저 발견한 홈의 위치
    holes = 0  # 자물쇠의 홈 갯수

    for i in range(N):
        for j in range(N):
            if lock[i][j] == 0:
                if (x, y) == (-1, -1):
                    x, y = i, j
                holes += 1
    
    # 홈이 아예 없다면 바로 True 반환
    if holes == 0:
        return True
    

    def check(key) -> bool:
        """
        위에서 저장한 홈 (x, y)는 무조건 채워져야하므로, 이 홈을 기준으로 키 맵을 끼워맞춘다.
        각 회전당 가능한 범위만큼 상하좌우 이동을 실행하고, 조건에 부합하는 경우가 있다면 바로 True를 반환.
        """

        # (x, y)가 가장 오른쪽, 가장 아래에 위치했을때도 가정하여 범위 설정
        for i in range(x - (M-1), x + 1):
            for j in range(y - (M-1), y + 1):
                cnt = 0  # (i, j)를 시작점으로 잡았을때 들어맞는 자물쇠 홈의 갯수
                flag = False  # 돌기와 돌기가 맞닿는지 판별

                for r in range(M):
                    cx = i + r

                    for c in range(M):
                        cy  = j + c

                        # 만약 해당 좌표가 자물쇠를 벗어난다면, 굳이 판별하지 않아도 되므로 pass
                        if not (0 <= cx < N and 0 <= cy < N):
                            continue

                        # 자물쇠, 열쇠 모두 돌기일경우 flag 체크 후 반복문 중단. 다음 (i, j)로 넘어가기.
                        if lock[cx][cy] == 1 and key[r][c] == 1:
                            flag = True
                            break
                        
                        # 열쇠의 돌기가 자물쇠의 홈에 들어맞는 경우 카운팅
                        if lock[cx][cy] == 0 and key[r][c] == 1:
                            cnt += 1
                    
                    # 다음 (i, j)로 넘어가기
                    if flag:
                        break
                
                # 조건에 부합(돌기끼리 맞닿지 않음)하고, 카운팅한 수가 자물쇠의 전체 홈의 갯수와 일치할경우 True 반환.
                # 🚨 중간에 break 당했을 경우, flag가 True여도 cnt == holes를 만족할수도 있으므로 not flag를 꼭 확인해줘야함.
                if not flag and cnt == holes:
                    return True
                
        return False
    

    for _ in range(4):
        if check(key):
            return True
        
        # 상하좌우 탐색이 끝날때마다 키 맵을 90º씩 회전
        key = [[key[M-1-j][i] for j in range(M)] for i in range(M)]
    
    return False