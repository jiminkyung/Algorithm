def solution(arr, idx):
    result = []
    for i in range(len(arr)):
        if i >= idx and arr[i] == 1:
            result.append(i)
    return min(result) if result else -1

# 몰랐던 함수 기능!
# index의 두번째 인자는 시작인덱스를 의미한다.
def solution(arr, idx):
    answer = 0
    try:
        answer = arr.index(1, idx)
    except:
        answer = -1
    return answer