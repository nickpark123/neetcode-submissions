class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openers = ["(", "{", "["]
        closers = [")", "}", "]"]
        for ch in s:
            if ch in openers:
                stack.append(ch)
            elif ch in closers:
                if not stack: 
                    return False
                idx = closers.index(ch)
                if stack[-1] != openers[idx]:
                    return False
                stack.pop()

        return len(stack) == 0
                

            
        

            

        