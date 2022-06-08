class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            d={}
            for i in range(len(s)):
                if s[i] in d:
                    d[s[i]] += 1
                else:
                    d[s[i]] = 1
            for i in range(len(t)):
                if t[i] not in d:
                    return False
                else:
                    d[t[i]] -= 1
        for value in d.values():
            if value != 0:
                return False
        return True