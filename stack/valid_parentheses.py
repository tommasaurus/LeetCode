class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {
                ")" : "(",
                "]" : "[",
                "}" : "{"
                }

        open_stack = []
        for each in s:
            if each in mapping:
                if len(open_stack) > 0:
                    recent = open_stack.pop()
                else:
                    return False
                    
                if recent != mapping[each]:
                    return False
            else:
                open_stack.append(each)
        
        return len(open_stack) == 0