# 구현
# 문자열
# 브루트포스 알고리즘


# 문제: https://www.acmicpc.net/problem/1907
# 메모리: 32412KB / 시간: 36ms
from sys import stdin


input = stdin.readline

def main():
    data = input().rstrip()
    X1, X = data.split("+")
    X2, X3 = X.split("=")

    def counting(X: str) -> dict[str: int]:
        """ 원자 갯수 계산 """
        X_dict = {"C": 0, "H": 0, "O": 0}  # 주어지는 원자 종류는 C, H, O 세개뿐임

        i = 0
        while i < len(X):
            if X[i].isdigit():
                X_dict[X[i-1]] += int(X[i])-1
            else:
                X_dict[X[i]] += 1
            i += 1
        return X_dict
    
    
    X1_dict = counting(X1)
    X2_dict = counting(X2)
    X3_dict = counting(X3)
    
    # 🚨최대공약수&최소공배수를 사용할 수 있지 않을까? 했지만 너무 복잡해짐.
    # 🗝️어차피 계수는 10이 최대이기 때문에, 각 식의 계수를 1~10 사이의 범위로 가정 후 계산해본다.
    # 사전순으로 가장 앞선것을 출력해야 하므로 X1부터 차례대로 대입해야함.
    for X1 in range(1, 11):
        for X2 in range(1, 11):
            for X3 in range(1, 11):
                if (X1_dict["C"]*X1 + X2_dict["C"]*X2 == X3_dict["C"]*X3 and
                X1_dict["H"]*X1 + X2_dict["H"]*X2 == X3_dict["H"]*X3 and
                X1_dict["O"]*X1 + X2_dict["O"]*X2 == X3_dict["O"]*X3):
                    print(X1, X2, X3)
                    return


main()