class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Approach: Iterate through each number in the array. For each number, start a streak using the number as the height for the streak. For each streak, check if it reaches and then add one. If the streak ends, compute the area and compare with the max. 
        

        # Approach: Create a stack and iterate through each number in the array. For each bar, add the index of the bar to the stack if the bar is higher or equal to the top value of the stack. If less, pop from the stack until the bar is higher than or equal to the top. Compare each area with the max.

        area = 0
        stack = []
       

        while stack:
            height = stack.pop()[1]
            width = len(heights) if not stack else len(heights) - stack[-1][0] - 1
            area = max(area, height * width)
        
        return area
        