class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.chars = characters
        self.n = combinationLength
        self.get_combinations(self.chars,self.n)
    
    def get_combinations(self,chars,n):
        self.res = []
        def dfs(path,c):
            if len(path) == n:
                self.res.append(path)
            for i in range(len(c)):
                dfs(path+c[i],c[i+1:])
        dfs('',chars)
        self.res_len = len(self.res)
        # print(self.res)

    def next(self) -> str:   
        out = self.res[0]
        self.res.pop(0)
        self.res_len -= 1
        return out
    
        
    def hasNext(self) -> bool:
        if self.res_len > 0:
            return True
        else:
            return False
        


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()