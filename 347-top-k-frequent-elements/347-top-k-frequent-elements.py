class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            if nums[i] in d:
                d[nums[i]] += 1
            else:
                d[nums[i]] = 1
        out = []
        for key,value in d.items():
            out.append([key,value])
        # print(out)
        # print(sorted(out, reverse = True, key = lambda x: x[1]))
        return [num[0] for num in sorted(out, reverse = True, key = lambda x: x[1])[:k]]
            