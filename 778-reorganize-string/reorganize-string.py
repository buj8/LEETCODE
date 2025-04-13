class Solution:
    def reorganizeString(self, s: str) -> str:
        counter = Counter(s)
        maxheap = []
        for item in counter:
            heapq.heappush(maxheap, [-counter[item], item])
        
        prev = None
        res = ""
        while maxheap:
            curr = heapq.heappop(maxheap)
            curr[0] += 1
            res += curr[1]
            if prev:
                heapq.heappush(maxheap, prev)
            if curr[0] < 0:
                prev = curr
            else:
                prev = None

        if len(res) == len(s):
            return res
        return ""