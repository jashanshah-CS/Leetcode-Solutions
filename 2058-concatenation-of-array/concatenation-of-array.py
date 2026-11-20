class Solution(object):
    def getConcatenation(self, nums):
        ans_length = 2 * len(nums)
        ans = []
        k=0
        ans.append(nums[k])
        for i in range(ans_length - 1):
            k+=1
            if k >= len(nums) :
                k = 0
            ans.append(nums[k])
        return ans
        