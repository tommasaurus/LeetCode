class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def recurse(combination, open_count, close_count, num, result):             
            if close_count == num:
                result.append(combination)
            else:
                if close_count < open_count:
                    recurse(combination + ")", open_count, close_count + 1, num, result)
                if open_count < num:
                    recurse(combination + "(", open_count + 1, close_count, num, result)
            return result
        
        return recurse("", 0, 0, n, [])