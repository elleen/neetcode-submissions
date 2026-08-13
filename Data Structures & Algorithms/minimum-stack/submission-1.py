class MinStack:

    def __init__(self):
        self.stack = list()
        self.minimum = list()

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.minimum) == 0:
            self.minimum.append(val)
        else:
            self.minimum.append(min(val, self.minimum[-1]))
        #print('pushed {}; stack = {}; min = {}'.format(val, self.stack, self.minimum))

    def pop(self) -> None:
        self.minimum.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minimum[-1]
