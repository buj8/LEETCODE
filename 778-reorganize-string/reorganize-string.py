class LetterCount(object):
    def __init__(self, letter, count):
        self.letter = letter
        self.count = count

    def __repr__(self):
        return f"{self.letter}: {self.count}"

    def __lt__(self, other):
        return self.count > other.count

class Solution:
    def reorganizeString(self, s: str) -> str:
        # IDEA:
        # MaxHeap ordered by the amount of letters left
        #   [example] > "aaaabbbccde" [4, 3, 2, 1, 1]
        # We pick the top one, append it's value and store it as "latest"
        # Repeat the same on the next iteration and
        counter = Counter(s)
        maxHeap = []

        for item in counter:
            lcount = LetterCount(item, counter[item])
            heapq.heappush(maxHeap, lcount)

        res = ""

        latest = None
        while maxHeap:
            nextLC = heapq.heappop(maxHeap)
            res += nextLC.letter
            if latest and latest.count > 0:
                heapq.heappush(maxHeap, latest)
            nextLC.count -= 1
            latest = nextLC
        
        return res if len(res) == len(s) else ""


        