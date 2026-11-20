class Solution(object):

  def findDisappearedNumbers(self, nums):
    seen = set(nums)
    result = []
    for x in range(1, len(nums) + 1):
      if x not in seen:
        result.append(x)
    return result