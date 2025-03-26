class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = defaultdict(int)
        for num in nums:
            frequency[num] += 1 

        freqlist = [[] for _ in range(len(nums) + 1)]
        for num, freq in frequency.items():
            freqlist[freq].append(num)
        
        topfreqs = []
        for i in reversed(freqlist):
            if i:
                topfreqs.extend(i)
                if k <= len(topfreqs):
                    return topfreqs[:k]  
