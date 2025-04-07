class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        current_index = 0
        prefix = ""
        if not strs or not strs[0]:
            return prefix

        while True:
            if current_index == len(strs[0]):
                return prefix
            letter = strs[0][current_index]

            for s in strs:
                if len(s) == current_index or s[current_index] != letter:
                    print(s, current_index, letter)
                    return prefix

            prefix += letter
            current_index += 1                 
            
            