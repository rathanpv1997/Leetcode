class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for i in range(len(strs)):
            if ''.join(sorted(strs[i])) in d:
                d[''.join(sorted(strs[i]))].append(strs[i])
            else:
                d[''.join(sorted(strs[i]))] = [strs[i]]
        return [value for value in d.values()]
            