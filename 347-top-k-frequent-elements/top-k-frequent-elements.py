class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = defaultdict(int)
        for num in nums:
            frequency[num] += 1 
        freqlist = []
        for num, freq in frequency.items():
            freqlist.append([num, freq])
        freqlist.sort(key=lambda x: x[1], reverse=True)
        topfreqs = []
        for i in range(k):
            topfreqs.append(freqlist[i][0])
        return topfreqs
