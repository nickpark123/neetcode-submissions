class TimeMap:

    def __init__(self):
        self.myMap = {}
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.myMap:
            self.myMap[key] = []
        self.myMap[key].append([value, timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        result = ""
        if key not in self.myMap:
            return result

        l, r, = 0, len(self.myMap[key])-1 
        while l <= r:
            m = (l + r) // 2
            if self.myMap[key][m][1] <= timestamp:
                result = self.myMap[key][m][0]
                l = m + 1
            else:
                r = m - 1
        return result

        
