class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freq = {}
        for each in nums:
            if each in freq:
                freq[each] += 1
            else:
                freq[each] = 1
        
        reverse_freq = {}
        for key, value in freq.items():
            if value in reverse_freq:
                reverse_freq[value].append(key)
            else:
                reverse_freq[value] = [key]
        
        keys = sorted(reverse_freq.keys(), reverse= True)
        answer = []

        index = 0
        while k > 0:
            key = keys[index]
            if len(reverse_freq[key]) <= k:
                answer.extend(reverse_freq[key])
                k -= len(reverse_freq[key])
                index += 1
            else:
                for i in range(k):
                    answer.append(reverse_freq[key][i])
            
        
        return answer
            
