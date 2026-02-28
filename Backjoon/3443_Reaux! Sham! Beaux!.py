# 구현
# 자료 구조
# 문자열
# 해시를 사용한 집합과 맵


# 문제: https://www.acmicpc.net/problem/3443

# 입력값 파싱때문에 애먹은 문제...
# 메모리: 37144KB / 시간: 64ms
from sys import stdin


def main():
    # rock: 0, scissors: 1, paper: 2
    rcp = {"cs": {"Kamen": 0, "Nuzky": 1, "Papir": 2}, "en": {"Rock": 0, "Scissors": 1, "Paper": 2},
            "fr": {"Pierre": 0, "Ciseaux": 1, "Feuille": 2}, "de": {"Stein": 0, "Schere": 1, "Papier": 2},
            "hu": {"Ko": 0, "Koe": 0, "Ollo": 1, "Olloo": 1, "Papir": 2},
            "it": {"Sasso": 0, "Roccia": 0, "Forbice": 1, "Carta": 2, "Rete": 2},
            "jp": {"Guu": 0, "Choki": 1, "Paa": 2}, "pl": {"Kamien": 0, "Nozyce": 1, "Papier": 2},
            "es": {"Piedra": 0, "Tijera": 1, "Papel": 2}}
    

    def calc(p1: int, p2: int) -> int:
        """ p1플레이어의 값과 p2플레이어의 값을 비교 후, 승자 반환 (p1: 0, p2: 1) """
        if p1 == p2:
            return -1
        
        if p1 == 0 and p2 == 2:
            return 1
        
        if p1 == 2 and p2 == 0:
            return 0
        
        if p1 > p2:
            return 1
        
        if p1 < p2:
            return 0
    

    # 🚨 처음엔 "-" 기준으로 나눈 후 turn별로 처리했는데 25%에서 탈락.
    # 그냥 한줄씩 받아서 while문으로 순회하니 통과했다.
    data = stdin.read().splitlines()
    turn = 1

    i = 0

    while i < len(data):
        # 각 턴 사이에 빈 줄
        if turn > 1:
            print()

        # 플레이어가 쓰는 언어, 이름
        p1_lang, p1_name = data[i].split()
        p2_lang, p2_name = data[i+1].split()
        i += 2
        point = [0, 0]

        while data[i] not in (".", "-"):
            p1, p2 = data[i].split()
            p1 = rcp[p1_lang][p1]
            p2 = rcp[p2_lang][p2]

            winner = calc(p1, p2)
            if winner != -1:
                point[winner] += 1

            i += 1

        # 🚨 포인트가 정확히 1점일때에만 "point"로 출력. 나머진 다 "points"로 출력.
        print(f"Game #{turn}:")
        print(f"{p1_name}: {point[0]} {"point" if point[0] == 1 else "points"}")
        print(f"{p2_name}: {point[1]} {"point" if point[1] == 1 else "points"}")

        if point[0] == point[1]:
            print("TIED GAME")
        else:
            winner = p1_name if point[0] > point[1] else p2_name
            print(f"WINNER: {winner}")
        
        if data[i] == ".":
            break

        turn += 1
        i += 1


main()