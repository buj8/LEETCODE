class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        nums.sort(reverse=True)
        self.k = k
        self.heap = []
        for i in range(min(len(nums), self.k)):
            heapq.heappush(self.heap, nums[i])  
        

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        # Pop the k + 1 largest
        while len(self.heap) > self.k:
            heapq.heappop(self.heap)
        # Return the k largest
        return self.heap[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)