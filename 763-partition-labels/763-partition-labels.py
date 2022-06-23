from collections import deque

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        n = len(s)
        if n == 1:
            return [1]
        res = []
        d = {letter:i for i,letter in enumerate(s)}
        # print(d)
        left,right = 0,0
        for i,letter in enumerate(s):
            right = max(right,d[letter])
            if i == right:
                res.append(right-left+1)
                left = i+1
        return res
        
        
            
            