class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = defaultdict(int)
        for num in nums:
            frequency[num] += 1 

        freqlist = [[] for i in range(len(nums) + 1)]
        for num, freq in frequency.items():
            freqlist[freq].append(num)
        
        topfreqs = []
        for i in reversed(freqlist):
            for num in i:
                topfreqs.append(num)
                if k == len(topfreqs):
                    return topfreqs  
