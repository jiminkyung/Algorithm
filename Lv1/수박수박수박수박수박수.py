def solution(n):
    subak = "수박"
    return subak*(n//2) if n%2==0 else subak*(n//2)+subak[0]

# 처음풀이
def solution(n):
    return "".join("수박"[i%2] for i in range(n))