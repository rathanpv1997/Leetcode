class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n <= 1:
            return n
        d = {}
        max_length = 0
        l = 0
        for r in range(n):
            if s[r] not in d:
                max_length = max(max_length,r-l+1)
            else:
                if d[s[r]] >= l:
                    l = d[s[r]]+1
                else:
                    max_length = max(max_length,r-l+1)
            d[s[r]] = r
        return max_length
                