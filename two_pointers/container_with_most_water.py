class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area = 0
        left = 0
        right = len(height) - 1
        while left < right:
            left_height = height[left]
            right_height = height[right]
            
            h = min(left_height, right_height)
            w = right - left            
            area = h * w

            max_area = max(area, max_area)
            if left_height < right_height:
                left += 1
            elif left_height > right_height:
                right -= 1
            else:
                left += 1
                right -= 1

        return max_area