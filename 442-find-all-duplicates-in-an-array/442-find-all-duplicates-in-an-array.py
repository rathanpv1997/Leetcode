class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        # d = {}
        # for i in nums:
        #     if i in d:
        #         d[i] += 1
        #     else:
        #         d[i] = 1
        # # print(d)
        # out = []
        # for key,value in d.items():
        #     # print(key,value)
        #     if value == 2:
        #         out.append(key)
        # return out
        res = []
        for x in nums:
            if nums[abs(x)-1] < 0:
                res.append(abs(x))
            else:
                nums[abs(x)-1] = -1*nums[abs(x)-1]
        return res