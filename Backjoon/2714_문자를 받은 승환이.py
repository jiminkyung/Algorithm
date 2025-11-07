# 구현
# 문자열


# 문제: https://www.acmicpc.net/problem/2714

# 2713_규현이의 사랑을 담은 문자메시지 와 이어지는 문제.
# 마찬가지로 구현 연습하기 좋음~
# 메모리: 32412KB / 시간: 32ms
from sys import stdin


input = stdin.readline

def main():
    T = int(input())
    # 5자리 2진수 비트 문자열: 알파벳 형태로 맵핑
    mapping = {bin(i)[2:].zfill(5): chr(i+64) for i in range(1, 27)}
    mapping["00000"] = " "

    def solve(R: int, C: int, M: str) -> str:
        # 동남서북 방향으로 진행
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        d = 0  # 초기 방향값

        # C, R-1, C-1, R-2... 만큼씩 상하좌우 이동.
        length = [R-1, C]
        l = 1
        words = ""
        x, y = 0, -1
        cnt = 0  # 확인한 문자 갯수

        # 나선형으로 배치된 값들을 원래 순서대로 words에 저장
        while cnt < len(M):
            for _ in range(length[l]):
                x += dx[d]
                y += dy[d]

                # 배열로 변환했을때 (x, y) 위치에 있는 값
                words += M[x*C+y]
                cnt += 1

            length[l] -= 1
            l ^= 1
            d = (d + 1) % 4
        
        ret = ""
        
        # 5자리씩 끊어서 맵핑
        for i in range(0, R*C, 5):
            line = words[i: i+5]
            # 문자의 총 길이 <= R*C 이므로, 남은 line의 길이가 5개 미만이라면 끝.
            if len(line) < 5:
                break
            ret += mapping[line]
        return ret.rstrip()


    for _ in range(T):
        R, C, M = input().rstrip().split()
        print(solve(int(R), int(C), M))


main()