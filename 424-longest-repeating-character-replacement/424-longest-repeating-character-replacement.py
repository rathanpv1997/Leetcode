class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        if n<=k:
            return n
        d = {}
        l=0
        max_same_char = 1
        for r in range(n):
            if s[r] in d:
                d[s[r]] += 1
                max_same_char = max(max_same_char,d[s[r]])
            else:
                d[s[r]] = 1
            if (r-l+1)-max_same_char<=k:
                max_window = r-l+1
            else:
                d[s[l]] -= 1
                l += 1
        return max_window
            
            
                