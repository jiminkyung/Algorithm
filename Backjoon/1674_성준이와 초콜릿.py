# 구현
# 정렬


# 문제: https://www.acmicpc.net/problem/1674

# 매번 초콜릿, 커피 적용시간을 계산하는게 비효율적이라고 생각했음.
# -> 쿼리를 순회하며 해당 시간(T)까지 초콜릿, 커피 계산값을 누적시킬 수 있나? 싶었지만 안됨.

# => 안전거리는 매 시간에 대해서만 구해야 함.
# => 만약 현재 T분이고 4분 전에 커콜릿을 먹었다면, "T-4분에 커콜릿을 먹었을때의 값"만 구해야 함. "T-4 ~ T분 사이의 거리 누적 값"을 구하는게 아님!!!
# 다시 풀어볼만한 문제~

# 메모리: 33432KB / 시간: 220ms
from sys import stdin


def main():
    data = stdin.read().splitlines()
    data.sort(key=lambda x: int(x.split()[1]))  # 시간(T)순으로 오름차순 정렬

    query = []
    choco = []
    coffee = []

    for d in data:
        d = d.rstrip().split()
        if d[0] == "Query":
            query.append(int(d[1]))
        else:
            t = int(d[1])
            n = float(d[2])
            if d[0] == "Chocolate":
                choco.append((t, n))
            else:
                coffee.append((t, n))
    
    # 매 쿼리마다 시간 확인 후, 해당 시간에 적용되는 초콜릿과 커피의 인덱스를 기록함.
    choco_idx = coffee_idx = 0

    for time in query:
        curr = 0.0

        # T에 적용되는 경우도 +1을 해주므로 실질적으로 적용 가능한 인덱스는 idx-1 까지임.
        while choco_idx < len(choco) and choco[choco_idx][0] <= time:
            choco_idx += 1
        while coffee_idx < len(coffee) and coffee[coffee_idx][0] <= time:
            coffee_idx += 1
        
        # 기록한 인덱스까지 초콜릿, 커피 안전거리 계산
        for i in range(choco_idx):
            t, n = choco[i]
            curr += max(0.0, 8*n - (time-t)/12)
        
        for i in range(coffee_idx):
            t, n = coffee[i]
            curr += max(0.0, 2*n - (time-t)**2/79)
        
        curr = max(1.0, curr)
        print(f"{time} {curr:.1f}")  # 소수점 두번째 자리에서 반올림


main()