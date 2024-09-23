class Solution(object):
    def isValid(self, character):
        numbers = set(["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])        
        if (ord(character) - ord("a") >=0 and ord(character) - ord("a") <= 25) or (character in numbers):
            return True
        return False

    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """        
        start = 0
        end = len(s) - 1
        while start < end:
            if not self.isValid(s[start].lower()):
                start += 1
            elif not self.isValid(s[end].lower()):
                end -= 1
            elif s[start].lower() != s[end].lower():
                return False
            else:    
                start += 1
                end -= 1
            
        return True