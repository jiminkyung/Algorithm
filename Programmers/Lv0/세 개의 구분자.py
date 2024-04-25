import re

def solution(myStr):
    result = re.sub("[abc]", " ", myStr)
    return result.split() if result.split() else ["EMPTY"]

# re를 사용한 더 간단한 방법!
import re

def solution(myStr):
    return re.findall(r"[^abc]+", myStr) or ["EMPTY"]