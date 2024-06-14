# 정렬
# 시간: 40ms
# 이렇게 메서드만 사용해서 풀어도 되나?

nums = []

for _ in range(5):
    nums.append(int(input()))

nums.sort()
print(sum(nums)//5, nums[2], sep="\n")