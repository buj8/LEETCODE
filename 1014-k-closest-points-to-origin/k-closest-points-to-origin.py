class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pdist = defaultdict(list)
        heap = []
        for point in points:
            dist = point[0] * point[0] + point[1] * point[1] # No need to calculate the sqrt, we're just ordering
            if len(heap) < k:
                heapq.heappush(heap, -dist)
                pdist[dist].append(point)
            elif dist < -heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, -dist)
                pdist[dist].append(point)

        res = []
        for item in heap:
            res.append(pdist[-item].pop())

        return res