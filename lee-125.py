class Solution:
    def alphaNum(self, c):
        return (("a" <= c.lower() <= "z") or ("0" <= c <= "9"))

    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1

        while l < r:
            while l < r and not self.alphaNum(s[l]):
                l += 1
            while r > l and not self.alphaNum(s[r]):
                r -= 1

            if s[l].lower() != s[r].lower():
                return False

            l, r = l+1, r-1
        return True
