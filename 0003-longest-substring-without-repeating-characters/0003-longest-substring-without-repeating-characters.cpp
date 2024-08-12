class Solution {
public:
    int lengthOfLongestSubstring(std::string s) {
        int n = s.length();
        if (n == 0) return 0;
        
        int start = 0, end = 0, maxlen = 0;
        std::unordered_map<char, int> charIndexMap;

        while (end < n) {
            char currentChar = s[end];
            if (charIndexMap.find(currentChar) != charIndexMap.end() && charIndexMap[currentChar] >= start) {
                start = charIndexMap[currentChar] + 1;
            }
            charIndexMap[currentChar] = end;
            maxlen = std::max(maxlen, end - start + 1);
            end++;
        }

        return maxlen;
    }
};