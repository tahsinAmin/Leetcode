class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for i in range(0, (len(ransomNote))):
            if ransomNote[i] in magazine:
                magazine = magazine.replace(ransomNote[i], "", 1)
            else:
                return False

        return True

# def checkRansom(ransomNote, magazine):
#     dic = {}
#     if len(ransomNote) > len(magazine):
#         return False
#     for char in magazine:
#         if char in dic:
#             dic[char] += 1
#         else:
#             dic[char] = 1
#     for char in ransomNote:
#         if char in dic and dic[char] > 0:
#             dic[char] -= 1
#         else:
#             return False
#     return True


# ransomNote = "aa"
# magazine = "aba"
# print(checkRansom(ransomNote, magazine))
