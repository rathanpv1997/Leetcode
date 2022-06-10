class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join([c if 97 <= ord(c) <= 122 or 48 <= ord(c) <= 57 else '' for c in s.lower()])
        # print(s)
        if len(s) == 1:
            return True
        l,r=0,len(s)-1
        while l<=r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return False
        return True
                
            