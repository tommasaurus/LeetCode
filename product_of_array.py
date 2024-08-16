class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left = [1] * len(nums)
        right = [1] * len(nums)

        left_product = 1
        right_product = 1
        for i, each in enumerate(nums):
            left[i] *= left_product 
            left_product *= each

        for i in range(len(nums) - 1, -1, -1):
            left[i] *= right_product
            right_product *= nums[i]

        return left