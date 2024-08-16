class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        unique = set()
        for each in nums:
            if each in unique:
                return True
            else:
                unique.add(each)

        return False