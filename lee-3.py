class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substr=""
        max_len = 0
        
        for ch in s:
            if ch not in substr:
                substr += ch
            else:
                max_len = max(max_len, len(substr))
                that_index = substr.index(ch)
                substr = substr[that_index+1:] + ch
        return max(max_len, len(substr))