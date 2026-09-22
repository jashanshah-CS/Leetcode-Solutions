class Solution(object):

  def findErrorNums(self, nums):
    dup = -1
    seen = set()
    for x in nums:
      if x in seen:
        dup = x
      seen.add(x)
    n = len(nums)
    for i in range(1, n + 1):
      if i not in seen:
        missing = i
        break

    return [dup, missing]