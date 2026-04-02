# 정렬
# 스위핑


# 문제: https://www.acmicpc.net/problem/3845
# 메모리: 33432KB / 시간: 36ms
from sys import stdin


def main():
    data = stdin.read().splitlines()[:-1]


    def check(coords: list[float], limit: float) -> bool:
        # 가장자리를 못 깎은 상태라면 바로 False
        if coords[0][0] > 0.0 or coords[-1][1] < limit:
            return False
        
        # 현재까지 깎은 최대좌표
        end = coords[0][1]

        for i in range(1, len(coords)):
            min_coord, max_coord = coords[i]

            # 틈이 발생한다면 False 반환
            if min_coord > end:
                return False
            
            end = max_coord
        return True


    for i in range(0, len(data), 3):
        _, _, w = data[i].split()
        w = float(w)
        size = w / 2

        # 🚨 요 부분때문에 삽질함.
        # 처음엔 map(float, sorted())로 작성했는데, 이렇게 되면 숫자 기준 정렬이 아닌 문자 기준 정렬이 되어버림.
        # 그래서 100.0이 들어와도, 정렬하면 맨 뒤가 아닌 2.xxx 전에 위치하게 됨.
        # 아래와 같이 변환 후 sort 해야 숫자 기준으로 안전하게 정렬 가능. (아님 check에서 하거나)
        x = [(xi - size, xi + size) for xi in sorted(map(float, data[i+1].split()))]
        y = [(yi - size, yi + size) for yi in sorted(map(float, data[i+2].split()))]
        
        x_ret = check(x, 75.0)
        y_ret = check(y, 100.0)

        # 🚨 가로로도 최소로도 한번씩 깎인 상태여야 함. 교집합이어야 한다는 소리.
        if x_ret and y_ret:
            print("YES")
        else:
            print("NO")


main()