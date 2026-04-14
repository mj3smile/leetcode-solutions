func twoSum(nums []int, target int) []int {
    diffs := make(map[int]int)

    for i1, n := range nums {
        i2, exists := diffs[n]
        if exists {
            return []int{i1, i2}
        }
        diffs[target - n] = i1
    }

    return nil
}