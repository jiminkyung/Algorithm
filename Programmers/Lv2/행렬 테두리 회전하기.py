"""
참고 코드 👉 https://velog.io/@dlgosla/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-level2-%ED%96%89%EB%A0%AC-%ED%85%8C%EB%91%90%EB%A6%AC-%ED%9A%8C%EC%A0%84%ED%95%98%EA%B8%B0

square: 주어진 크기대로 만든 행렬
dx, dy: 위-오른쪽-아래-왼쪽 테두리 이동 방향
Pyalgo100의 청소 경로 문제와 비슷하다~
"""

def solution(rows: int, columns: int, queries: list) -> list:
    square = [[i*columns+k+1 for k in range(columns)]for i in range(rows)]
    ret = []

    for query in queries:
        x1, y1, x2, y2 = query
        x1, y1, x2, y2 = x1-1, y1-1, x2-1, y2-1
        _min = float("inf")

        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]

        x, y = x1, y1
        curr = square[x1][y1]
        direction = 0

        while True:
            nx = x + dx[direction]
            ny = y + dy[direction]

            if not x1 <= nx <= x2 or not y1 <= ny <= y2:
                if direction == 3:
                    break
                direction += 1
                continue

            _next = square[nx][ny]
            square[nx][ny] = curr
            curr = _next
            x, y = nx, ny

            if curr < _min:
                _min = curr

        ret.append(_min)
    return ret