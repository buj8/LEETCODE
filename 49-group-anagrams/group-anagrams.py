class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_words = defaultdict(list)

        for word in strs:
            sorted_word = ''.join(sorted(word))
            sorted_words[sorted_word].append(word)

        return [words for words in sorted_words.values()]