class CustomStack(object):

    def __init__(self, maxSize):
        """
        :type maxSize: int
        """
        self.maxSize = maxSize
        self.stack = []
        self.inc = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if len(self.stack) < self.maxSize:
            self.stack.append(x)
            self.inc.append(0)

    def pop(self):
        """
        :rtype: int
        """
        if not self.stack:
            return -1

        idx = len(self.stack) - 1
        increment_val = self.inc.pop()
        
        # Propagate the increment down to the preceding element
        if idx > 0:
            self.inc[idx - 1] += increment_val

        return self.stack.pop() + increment_val

    def increment(self, k, val):
        """
        :type k: int
        :type val: int
        :rtype: None
        """
        # Lazily apply the increment to the boundary element
        idx = min(k, len(self.stack)) - 1
        if idx >= 0:
            self.inc[idx] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)