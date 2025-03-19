func containsDuplicate(nums []int) bool {
    m := make(map[int]struct{})
    for _, num := range nums {
        _, in_m := m[num]
        if in_m {
            return true
        }
        m[num] = struct{}{}
    }
    return false
}