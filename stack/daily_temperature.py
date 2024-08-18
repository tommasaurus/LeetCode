class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)        
        for i, each in enumerate(temperatures):                       
            while stack and temperatures[stack[-1]] < each:
                index = stack.pop()
                result[index] = i - index
            stack.append(i)
            
        
        return result