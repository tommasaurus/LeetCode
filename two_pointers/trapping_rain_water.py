class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
            
        water = 0
        left = 0
        right = len(height) - 1
        left_max = 0
        right_max = 0
        while left < right:
            if height[left] <= height[right]:
                left_max = max(left_max, height[left])
                water += left_max - height[left]
                left += 1
            else:
                right_max = max(right_max, height[right])
                water += right_max - height[right]
                right -= 1

        return water