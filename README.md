# Arrays

- If you have to look through an element and compare with another element progresssively, use pointers

# Queue using array

```
    l = [1]
    for i in range(2, 10):
        l.insert(0, i)
    l.pop()
    print(l)
```

# Learned

```
    for char in m:
        if char in dic:
            dic[char] += 1
        else:
            dic[char] = 1

    ANS :
    dic = {}
    for char in m:
            dic[char] = 1 + dic.get(char, 0)
```

Leetcode 733 = https://youtu.be/mIp647XVRyc

# Problems

- Difference between Dynamic programming and Memoisation.

