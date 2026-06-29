class MinStack:

    def __init__(self):
        self.stack = []
        self.last = None
        self.mini = None

        self.track = []


    def push(self, val: int) -> None:
        self.stack.append(val)
        self.last = val
        if self.mini == None or self.mini > val:
            self.mini = val
            self.track.append(val)
        else:
            self.track.append(self.mini)

    def pop(self) -> None:
        if len(self.stack) > 1:
            self.last = self.stack[-2]
        else:
            self.last = None
        self.stack.pop(-1)
        self.track.pop(-1)
        
        if self.track:
            self.mini = self.track[-1]
        else:
            self.mini = None

    def top(self) -> int:
        return self.last
        
    def getMin(self) -> int:
        return self.track[-1]
        
