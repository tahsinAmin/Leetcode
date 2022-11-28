# Arrays

- If you have to look through an element and compare with another element progresssively, use pointers

# Learned

```
      for i in range(len_s):
        if s[i] in dict_s:
            dict_s[s[i]] += 1
        else:
            dict_s[s[i]] = 1

    ANS :
    for i in range(len_s):
        dict_s[s[i]] = 1 + dict_s.get(s[i], 0)
```

Leetcode 733 = https://youtu.be/mIp647XVRyc
