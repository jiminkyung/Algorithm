# 행렬 곱셈하는법!
# ret(11) == arr1(1n) * arr2(n1)
def solution(arr1, arr2):
    # ret = [[0] * len(arr2[0])] * len(arr1) => 초기화 문제.
    ret = [[0 for _ in range(len(arr2[0]))] for _ in range(len(arr1))]
    def matrix(row, col):
        mat_sum = 0
        for i in range(len(arr2)): # 처음에 len(arr1)로 했다가 런타임 오류. 당연함.
            # len(행렬1의 열) == len(행렬2의 행) 이어야 하므로 arr1[0]이나 arr2를 넣어야한다.
            mat_sum += arr1[row][i] * arr2[i][col]
        return mat_sum

    for row in range(len(arr1)):
        for col in range(len(arr2[0])):
            ret[row][col] = matrix(row, col)
    return ret