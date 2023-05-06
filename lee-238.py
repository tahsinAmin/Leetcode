# nums = [1, 2, 3, 4]
nums = [-1, 1, 0, -3, 3]

output = []

pre = 1

for i in range(len(nums)):
    output.append(pre)
    pre *= nums[i]

post = 1
for i in reversed(range(len(nums))):
    output[i] *= post
    post *= nums[i]

print(output)
