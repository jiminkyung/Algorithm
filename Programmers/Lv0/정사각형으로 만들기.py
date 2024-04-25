def solution(arr):
    row = len(arr)
    col = len(arr[-1])
    if row > col:
        for i in arr:
            i.extend([0]*(row-col))
    elif row < col:
        for _ in range(col-row):
            arr.append([0]*col)
    return arr

# 반례 [[1, 1], [1, 1], [1, 1], [1, 1]] => [[1, 1, 0], [1, 1, 0], [1, 1, 0], [1, 1, 0]]
# 행과 열의 차이수만큼 0을 추가해주는 방식으로 변경.