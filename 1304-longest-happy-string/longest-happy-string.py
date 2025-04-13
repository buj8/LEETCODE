class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        # Max heap to prioritize characters with higher frequency
        heap = []
        if a > 0:
            heapq.heappush(heap, [-a, 'a'])
        if b > 0:
            heapq.heappush(heap, [-b, 'b'])
        if c > 0:
            heapq.heappush(heap, [-c, 'c'])
        
        result = []
        
        while heap:
            # Get the most frequent character
            count, char = heapq.heappop(heap)
            
            # Check if we already have two consecutive identical characters
            if len(result) >= 2 and result[-1] == result[-2] == char:
                # Can't use the most frequent character, try the next one
                if not heap:
                    # No more characters left that we can use
                    break
                    
                # Get the next most frequent character
                next_count, next_char = heapq.heappop(heap)
                
                # Use it if there are any left
                if next_count < 0:
                    result.append(next_char)
                    next_count += 1
                    if next_count < 0:
                        heapq.heappush(heap, [next_count, next_char])
                
                # Put the original character back in the heap
                heapq.heappush(heap, [count, char])
            else:
                # Can use the most frequent character
                result.append(char)
                count += 1
                if count < 0:
                    heapq.heappush(heap, [count, char])
        
        return ''.join(result)