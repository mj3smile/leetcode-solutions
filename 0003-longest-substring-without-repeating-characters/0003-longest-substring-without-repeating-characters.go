func lengthOfLongestSubstring(s string) int {
    charIndexes := make(map[string]int)
    result := 0
    left := 0
    for right, r := range s {
        index, exist := charIndexes[string(r)]
        if exist {
            for left != index {
                delete(charIndexes, string(s[left]))
                left += 1
            }
            left += 1
        }

        charIndexes[string(r)] = right
        result = max(result, right - left + 1)
    }

    return result
}

func max(v1, v2 int) int {
    if v2 > v1 {
        return v2
    }
    return v1
}