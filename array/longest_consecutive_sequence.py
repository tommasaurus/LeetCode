class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        longest_sequence = 0
        num_set = set(nums)

        for each in nums:
            if each - 1 not in num_set:                            
                streak = 0
                while each in num_set:
                    streak += 1
                    each += 1

                longest_sequence = max(longest_sequence, streak)

        return longest_sequence