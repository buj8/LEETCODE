class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counterS = Counter(s)
        counterT = Counter(t)

        def are_counters_equal(a, b) -> bool:
            if len(a) != len(b):
                return False
            for k, v in a.items():
                if a[k] != b[k]:
                    return False
            return True

        return are_counters_equal(counterS, counterT)