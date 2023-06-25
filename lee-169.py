nums = [2,2,1,1,1,2,2]
res, cnt = nums[0], 1

for i in range(1, len(nums)):
    cnt += 1  if nums[i] == res else -1
    if cnt == 0:
        res = nums[i]
    
print(res)