class Solution(object):

  def buildArray(self, target, n):
    result = []
    for i in range(1, n + 1):
        if i > target[-1]:
            break
        found = False
        result.append("Push")
        for x in range(len(target)):
            if i == target[x]:
                found = True
                break
        if found == False:
            result.append("Pop")
    return result
