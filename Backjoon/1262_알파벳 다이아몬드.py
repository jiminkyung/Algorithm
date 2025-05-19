# 구현


# 문제: https://www.acmicpc.net/problem/1262

# 아뿔싸! N에 알맞는 다이아몬드 형태를 생성한 뒤, 패턴에 맞춰 계산하려고 했으나...
# N의 범위가 크다;; 다이아몬드 한개를 미리 만들어놓는것부터가 메모리 초과 각.
# 해결법👉 https://velog.io/@gobeul/%EB%B0%B1%EC%A4%80-1262-%EC%95%8C%ED%8C%8C%EB%B2%B3-%EB%8B%A4%EC%9D%B4%EC%95%84%EB%AA%AC%EB%93%9C-python-java
# => 중심을 기준으로 거리 계산 후, 거리값이 N 이하라면 알맞은 알파벳 삽입.

# 메모리: 32412KB / 시간: 52ms
from sys import stdin


input = stdin.readline

def main():
    N, R1, C1, R2, C2 = map(int, input().split())
    alphabet = [chr(97+i) for i in range(26)]
    
    D = 2*N - 1  # 패턴 하나의 가로, 세로 길이

    for i in range(R1, R2+1):
        line = ""
        for j in range(C1, C2+1):
            # 🚨 패턴은 반복되므로 (i, j)를 타일 크기로 나눠 상대 좌표로 변환
            i %= D
            j %= D

            # 중심으로부터 (i, j)까지의 맨해튼 거리 계산
            dis = abs(N-1 - i) + abs(N-1 - j)
            if dis > N-1:  # 범위 밖이면 . 삽입
                line += "."
            else:
                line += alphabet[dis % 26]  # a~z가 반복되므로 모듈러 처리
        print(line)


main()