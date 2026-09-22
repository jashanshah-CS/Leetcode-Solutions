class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        result = []
        count = 0
        for i in range(len(nums)):
            count = 0
            for j in range(len(nums)):
                if nums[i] > nums[j]:
                    count+=1
            result.append(count)
        return result

        