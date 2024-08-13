class Solution {
public:
    bool isAnagram(string s, string t) {
        std::unordered_map<char, int> original;
        for(char& letter : s) {
            original[letter] += 1;
        }
        for(char& letter : t) {
            original[letter] -= 1;
            if (original[letter] == 0) {
                original.erase(letter);
            }
        }
        return original.empty();
    }
};