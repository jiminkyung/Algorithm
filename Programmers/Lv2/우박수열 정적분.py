"""
콜라츠 추측 == 우박수열
k: 우박수의 초항, ranges: 정적분을 구하는 구간들 목록
단, 구간의 시작점이 끝점보다 커질 경우 -1.0를 반환해야함.
인접한 두 점 (x1, y1)과 (x2, y2)사이의 면적 = |x2 - x1| * (y1 + y2) / 2 = 사다리꼴 공식

정적분 구간은 전체 수열의 길이 기준으로 구해야함.
[0, -1] => 시작점: 0, 끝점: 길이 - 1
하지만 두 수열을 비교해가며 적분해야하기 때문에, 길이가 아닌 인덱스값을 기준으로 했음.
- 만약 길이를 기준으로 구한다면 nx = i + nx가 아닌 nx = len(collatz) + nx 또는 (i+1) + nx
- 어차피 적분값 구할때 끝범위를 -1 해줘야 했으므로 그냥 nx = i + nx로 계산함.
- 나중에 왜 이렇게 썼나 고민하지 말아라...
"""

def solution(k: int, ranges: list) -> list:
    collatz = []
    integral = []

    # 콜라츠 수열 저장
    i = 0
    while k > 1:
        collatz.append((i, k))
        if k % 2 == 0:
            k //= 2
        else:
            k = k * 3 + 1
        i += 1
    collatz.append((i, k))

    # 정적분 수행
    for x, nx in ranges:
        nx = i + nx  # 콜라츠 수열에서 사용했던 i(횟수)
        if x > nx:
            integral.append(-1.0)
        else:
            tmp = 0.0
            for k in range(x, nx):
                tmp += (collatz[k+1][1] + collatz[k][1]) / 2
            integral.append(tmp)
    return integral