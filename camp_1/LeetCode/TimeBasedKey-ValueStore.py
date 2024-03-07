class TimeMap:

    def __init__(self):
        self.hash_map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hash_map[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        arr = self.hash_map[key]
        low , high = 0 , len(arr) - 1
        ans = ["",-inf]


        while low <= high:
            mid = (low + high) // 2

            if arr[mid][0] <= timestamp and arr[mid][0] > ans[1]:
                ans[1] = arr[mid][0]
                ans[0] = arr[mid][1]
                low = mid + 1
            elif arr[mid][0] > timestamp:
                high = mid - 1
            else:
                low = mid + 1
        
        return  ans[0]


        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)