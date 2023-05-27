# Algorithms

- lee-98

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

```
for c in s:
    if c in dic:
        dic[c] +=1
    else:
        dic[c] = 1

ANS:
from collections import Counter
dic = Counter(s)
```

```
for i in dic.values():
    if i % 2 == 0:
        longest_len += i
    else:
        longest_len += i - 1
        odd_found = True


ANs:
for i in dic.values():
    if i % 2:
        odd_found = True
    longest_len += i - i % 2
```

- BFS
  - Lee 995 Rotting Oranges

## Extract value from list

```
    x,y,z = [1,2,3]
    print(y)
```

`Since I already know the list has 3 items and I nonly need the last 2 items, Now, I can easily work with y & z`

Leetcode 733 = https://youtu.be/mIp647XVRyc

## Switch Case

```
match item:
    case "+":
        stack.append(stack.pop() + stack.pop())
    case "-":
        y, x = stack.pop(), stack.pop()
        stack.append(x - y)
```

# Problems

- Difference between Dynamic programming and Memoisation.
