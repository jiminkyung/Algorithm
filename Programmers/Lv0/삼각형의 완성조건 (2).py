def solution(sides):
    return len([i for i in range(abs(sides[0]-sides[1])+1, sum(sides))])