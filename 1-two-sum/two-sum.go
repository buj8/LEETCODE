func twoSum(nums []int, target int) []int {

    m := make(map[int]int)

    for i1, val := range(nums){
        needed := target - val
        
        if i2, exists := m[needed]; exists {
            return []int{i1, i2}
        }

        m[val] = i1
    }

    return []int{}
}