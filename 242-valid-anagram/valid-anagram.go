func isAnagram(s string, t string) bool {
    letters := make(map[rune]int)
    for _, letter := range s {
        letters[letter] += 1
    }
    for _, letter := range t {
        letters[letter] -= 1
        if letters[letter] == 0 {
            delete(letters, letter) 
        }
    }
    return len(letters)==0
}