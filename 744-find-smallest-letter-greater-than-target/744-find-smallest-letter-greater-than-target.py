class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l,r=0,len(letters)-1
        if letters[-1] <= target:
            return letters[0]
        while l<r:
            mid = l + (r-l)//2
            if letters[mid] <= target:
                if letters[mid+1] > target and mid+1<len(letters):
                    return letters[mid+1]
                if letters[mid+1] <= target and mid+1<len(letters):
                    l = mid+1
            elif letters[mid] > target:
                r = mid
        return letters[mid]
        
            
                        