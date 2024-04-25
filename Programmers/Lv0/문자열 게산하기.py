def solution(my_string):
    return eval(my_string)

# 하지만 eval은 보안에 취약해서 실제로는 잘 안쓴다고 한다.
# 아래의 코드가 더 간지나는 것 같다.

def solution(my_string):
    return sum(int(i) for i in my_string.replace(' - ', ' + -').split(' + '))

# "3 - 5" 로 주어지면 "3 + -5"로 바꿔버려서 음수로 입력되게끔...ㅎㅎ