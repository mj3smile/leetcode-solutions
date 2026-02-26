var result [][]int
func permute(nums []int) [][]int {
    result = make([][]int, 0)
	calculate(nums, make([]int, 0), make(map[int]bool))
	return result
}

func calculate(nums, currResult []int, picked map[int]bool) {
	if len(currResult) == len(nums) {
        temp := append([]int{}, currResult...)
		result = append(result, temp)
	}

	for _, i := range nums {
		if picked[i] {
			continue
		}
		picked[i] = true
		currResult = append(currResult, i)
		calculate(nums, currResult, picked)
		picked[i] = false
		currResult = currResult[:len(currResult) - 1]
	}
}