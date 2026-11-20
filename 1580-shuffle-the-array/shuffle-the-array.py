class Solution(object):
    def shuffle(self, nums, n):
        first = nums[0:len(nums)/2]
        second = nums[len(nums)/2:]
        result = []
        for i,j in zip(first,second):
            result.append(i)
            result.append(j)
        return result
        