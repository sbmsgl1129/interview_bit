class MinStack:
    
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    
    # @param x, an integer
    def push(self, x):
        self.stack1.append(x)
        
        if not self.stack2 or self.stack2[-1] >= x:
            self.stack2.append(x)

    # @return nothing
    def pop(self):
        if self.stack1:
            last = self.stack1.pop()
            if last == self.stack2[-1]:
                self.stack2.pop()
    
    # @return an integer
    def top(self):
        if not self.stack1:
            return -1
        return self.stack1[-1]

    # @return an integer
    def getMin(self):
        if not self.stack2:
            return -1
        return self.stack2[-1]
