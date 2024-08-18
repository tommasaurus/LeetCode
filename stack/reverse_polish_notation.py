class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        number_stack = []
        operands = set(["+","-","*","/"])
        for each in tokens:
            if each in operands:
                second = int(number_stack.pop())
                first = int(number_stack.pop())
                result = None
                match each:
                    case "+":
                        result = first + second
                    case "-":
                        result = first - second
                    case "*":
                        result = first * second
                    case "/":
                        result = first / second
                number_stack.append(result)
            else:
                number_stack.append(each)
        
        return int(number_stack.pop())


        