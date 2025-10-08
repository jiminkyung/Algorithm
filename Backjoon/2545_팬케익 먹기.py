# 수학
# 그리디 알고리즘


# 문제: https://www.acmicpc.net/problem/2545

# 1점 -> 3점 업그레이드 성공 하하하
# 메모리: 32412KB / 시간: 32ms
from sys import stdin


input = stdin.readline

def main():
    T = int(input())

    for _ in range(T):
        input()
        # 🗝️ A, B, C가 평등하게끔 잘라나가야 함
        A, B, C, D = map(int, input().split())
        size = [A, B, C]
        size.sort()
        A, B, C = size

        gap = [C-B, B-A, A]

        # 만약 제일 큰 수 - 두번째로 큰 수의 차이가 D보다 크다면, 제일 큰 수 C를 조정하는 것 만으로도 D번을 채울 수 있다는것.
        if gap[0] >= D:
            C -= D
        # 아니라면 B까지 고려해봄
        else:
            # 일단 C를 B 크기만큼 자른다.
            C = B
            D -= gap[0]

            # 만약 C-A, B-A의 차이가 D보다 크다면, 두 수 B, C만 조정해서 D번을 채울 수 있음.
            if gap[1] * 2 >= D:
                # 최대한 균등하게 만들어줘야함.
                # ex) [1, 3, 3]이고 D가 1인 상황이라면? tmp는 2*2 - 1 = 3이 될 것임.
                # tmp = 1이 되므로 [1, 2, 2]가 만들어짐. 아지만 tmp % 2 == 1이니 [1, 2, 3]으로 수정.
                tmp = (gap[1] * 2 - D) // 2
                C = A + tmp
                B = A + tmp

                if (gap[1] * 2 - D) % 2 != 0:
                    C += 1
            # 아니라면 마지막 A까지 조정해야함. 허걱슨~
            else:
                # C, B를 A 크기만큼 자름
                C = B = A
                D -= gap[1] * 2

                # A, B, C 크기 조정
                if gap[2] * 3 >= D:
                    # B 조정할때와 같음. 최대한 균등하게.
                    tmp = (gap[2] * 3 - D) // 3
                    C = B = A = tmp

                    # 🚨 3으로 나누는것이므로 나머지가 2가 될 수도 있음. 고려해야함.
                    rest = (gap[2] * 3 - D) % 3
                    if rest == 1:
                        C += 1
                    if rest == 2:
                        C += 1
                        B += 1


        print(A * B * C)


main()