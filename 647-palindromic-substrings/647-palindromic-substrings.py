class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        res = ""
        count = 0
        dp = {}
        for i in range(n):
            l,r = i,i
            while l>= 0 and r <= n-1:
                if s[l] == s[r]:
                    count += 1
                    l -= 1
                    r += 1
                else: 
                    break
            l,r = i,i+1
            while l>= 0 and r <= n-1:
                if s[l] == s[r]:
                    count += 1
                    l -= 1
                    r += 1
                else: 
                    break
        return count
                
                
                    