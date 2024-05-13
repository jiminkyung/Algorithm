"""
맨해튼 거리: 두 테이블 T1, T2가 행렬 (r1, c1), (r2, c2)에 각각 위치하고 있다면,
T1, T2 사이의 맨해튼 거리는 |r1 - r2| + |c1 - c2| 이다.

아래는 AI에게 물어본 풀이. 대각선 체크하는 부분에서 헤매다가 결국ㅜㅜ
우선 각 자리를 순회한다음에, "P"에 해당하면 check 함수를 통해 체크.
조건에 맞지 않는다면(False) flag를 0으로 변경. 맞다면 그대로 1로 둔다.
각 place에 대한 검사가 끝날때마다 결과값 flag를 answer에 추가해준다.
"""

def check(place, r, c):
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1), (2, 0), (-2, 0), (0, 2), (0, -2)]
    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if 0 <= nr < 5 and 0 <= nc < 5 and place[nr][nc] == "P":
            if abs(dr) + abs(dc) == 1:  # 맨해튼 거리가 1
                return False
            elif abs(dr) + abs(dc) == 2:  # 맨해튼 거리가 2
                if dr == 0 or dc == 0:  # 직선상
                    if place[r + dr//2][c + dc//2] != "X":
                        return False
                else:  # 대각선상
                    if place[r][nc] != "X" or place[nr][c] != "X":
                        return False
    return True

def solution(places):
    answer = []
    for place in places:
        flag = 1
        for r in range(5):
            for c in range(5):
                if place[r][c] == "P" and not check(place, r, c):
                    flag = 0
                    break
            if flag == 0:
                break
        answer.append(flag)
    return answer