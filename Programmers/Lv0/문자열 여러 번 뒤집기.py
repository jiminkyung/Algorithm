def solution(my_string, queries):
    result = my_string
    for s, e in queries:
        result = result[:s] + result[s:e+1][::-1] + result[e+1:]
    return result
# 사실 중간에 result[s:e+1:-1]로 작성하는 바람에 무한 에러에 빠져버림...
# 다른분 코드를 참고했다ㅜㅜ 바보같은 짓을;;

# 다른 풀이. 리스트를 이용한 풀이인데 더 신박하다.
def solution(my_string, queries):
    answer=list(my_string)
    for s,e in queries:
        answer[s:e+1]=answer[s:e+1][::-1]
    return ''.join(answer)