def binary_search(nums, target):
    l, r = 0, len(nums)-1
    while l <= r:
        midIdx = l + (r-l)//2
        if nums[midIdx] == target:
            return midIdx
        elif nums[midIdx] > target:
            r = midIdx - 1
        else:
            l = midIdx + 1

    return -1


nums = [-1, 0, 3, 5, 9, 12]
target = 9

print(binary_search(nums, target))


#  The reason for not going  midIdx = (l + r)//2 and going with  midIdx = l + (r-l)//2 is because it may overflow if l and r are both very high value
