class Solution(object):
    def dailyTemperatures(self, temperatures):
        n = len(temperatures)
        result = [0] * n
        stack = [] 
        for current_day, current_temp in enumerate(temperatures):
            while stack and current_temp > temperatures[stack[-1]]:
                prev_day = stack.pop()
                result[prev_day] = current_day - prev_day
            stack.append(current_day)
        return result