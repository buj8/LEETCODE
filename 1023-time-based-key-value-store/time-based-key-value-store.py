class TimeMap:

    def __init__(self):
        self.maps = {}
        self.times = defaultdict(list)


    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.maps:
            self.maps[key] = {timestamp: value}
        else:
            self.maps[key][timestamp] = value
        self.times[key].append(timestamp)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.maps:
            return ""
            
        timestamps = self.times[key]
        
        if timestamp in self.maps[key]:
            return self.maps[key][timestamp]
            
        if timestamp < timestamps[0]:
            return ""
            
        if timestamp >= timestamps[-1]:
            return self.maps[key][timestamps[-1]]
        
        left, right = 0, len(timestamps) - 1
        result = -1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if timestamps[mid] <= timestamp:
                result = mid
                left = mid + 1
            else:
                right = mid - 1
        
        return self.maps[key][timestamps[result]]

                    

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)