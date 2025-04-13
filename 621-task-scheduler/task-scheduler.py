class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        max_heap = []
        for item in counter:
            heapq.heappush(max_heap, -counter[item])
        queue = deque([])

        time = 0

        while max_heap or queue:
            # Put all the tasks that have finished it's gap back in the heap
            while queue and queue[0][1] <= time:
                heapq.heappush(max_heap, queue.popleft()[0])
            
            # If we still don't have anything available, move to the next timeslot
            if not max_heap:
                time = queue[0][1]
           
            # If we do, complete a timeslot and move to the next interval
            else:
                time += 1 
                task = heapq.heappop(max_heap) + 1
                if task < 0:
                    queue.append((task, time + n))


        return time