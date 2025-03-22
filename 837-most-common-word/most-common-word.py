class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = paragraph.lower()
        
        punctuation_symbols = ["!", "?", "'", ",", ";", "."]
        
        for symbol in punctuation_symbols:
            paragraph = paragraph.replace(symbol, " ")
        
        words = {}
        most_common = ("", 0)
        
        for word in paragraph.split():
            if word not in banned:
                if word in words:
                    words[word] += 1
                else:
                    words[word] = 1
                
                if words[word] > most_common[1]:
                    most_common = (word, words[word])

        return most_common[0]