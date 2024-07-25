# 분할 정복

# 분할 정복 방법, 스택 구현 방법 두가지가 있다.
# 아래는 AI를 통해 얻어낸 풀이. 직접 풀이 X

# 1. 분할 정복 사용
def largest_rectangle_dc(heights, start, end):
    if start > end:
        return 0
    if start == end:
        return heights[start]
    
    mid = (start + end) // 2
    
    # 왼쪽과 오른쪽 부분에서의 최대 넓이
    left_area = largest_rectangle_dc(heights, start, mid)
    right_area = largest_rectangle_dc(heights, mid+1, end)
    
    # 중간을 걸치는 직사각형의 최대 넓이
    height = min(heights[mid], heights[mid+1])
    width = 2
    area = height * width
    left = mid - 1
    right = mid + 2
    
    while left >= start or right <= end:
        if right <= end and (left < start or heights[right] > heights[left]):
            height = min(height, heights[right])
            right += 1
        else:
            height = min(height, heights[left])
            left -= 1
        width += 1
        area = max(area, height * width)
    
    return max(left_area, right_area, area)

# 입력 처리
while True:
    inputs = list(map(int, input().split()))
    if inputs[0] == 0:
        break
    n, heights = inputs[0], inputs[1:]
    print(largest_rectangle_dc(heights, 0, n-1))


# 2. 스택 사용
def largest_rectangle(heights):
    stack = []
    max_area = 0
    heights.append(0)  # 마지막에 0을 추가해 모든 막대를 처리하도록 함
    
    for i, h in enumerate(heights):
        start = i
        while stack and stack[-1][1] > h:
            index, height = stack.pop()
            max_area = max(max_area, height * (i - index))
            start = index
        stack.append((start, h))
    
    return max_area

# 입력 처리
while True:
    inputs = list(map(int, input().split()))
    if inputs[0] == 0:
        break
    n, heights = inputs[0], inputs[1:]
    print(largest_rectangle(heights))