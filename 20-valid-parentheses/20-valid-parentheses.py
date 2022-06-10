class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False
        d = {'(':')','{':'}','[':']'}
        q = collections.deque()
        for bracket in s:
            if bracket in ['{','(','[']:
                q.append(bracket)
            if bracket in ['}',')',']']:
                if q:
                    if d[q.pop()] != bracket:
                        return False
                else:
                    return False
        if q:
            return False
        return True