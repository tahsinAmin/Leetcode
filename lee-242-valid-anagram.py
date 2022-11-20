def isAnagram(s, t):
    len_s, len_t = len(s), len(t)
    if len_s != len_t:
        return False

    countS, countT = {}, {}

    for i in range(len_t):
        countS[s[i]] = 1 + countS.get(s[i], 0)
        countT[t[i]] = 1 + countT.get(t[i], 0)

    for key in countS:
        if countS[key] != countT.get(key, 0):
            return False

    return True


s = "anagram"
t = "nagaram"
print(isAnagram(s, t))
