class MinStack(object):

    def __init__(self):
        self.stack = []
        self.min = []
        

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        if len(self.min) == 0:
            self.min.append(val)
        elif len(self.min) > 0 and self.min[-1] >= val:
           self.min.append(val)
         
        self.stack.append(val)
        

    def pop(self):
        """
        :rtype: None
        """
        if len(self.stack) > 0:
            popped = self.stack.pop()
            if popped == self.min[-1]:
                self.min.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.min[-1]
        

