class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        letters_count = dict() # key: letter in s, val: numbers of it in a window
        most_letter_in_window = ""
        result = 1

        left = 0
        for right in range(len(s)):
            curr_char = s[right]
            letters_count[curr_char] = letters_count.get(curr_char, 0) + 1
            if letters_count[curr_char] > letters_count.get(most_letter_in_window, 0):
                most_letter_in_window = curr_char
            
            window_len = right - left + 1
            if window_len == 1:
                continue
            
            if window_len - letters_count[most_letter_in_window] > k:
                letters_count[s[left]] -= 1
                most_letter_in_window = self.getMostLetter(letters_count)
                left += 1
                continue
            
            result = max(result, window_len)

        return result

    def getMostLetter(self, letters_count):
        max_count = 0
        result = ""

        for letter, count in letters_count.items():
            if count > max_count:
                max_count = count
                result = letter

        return result            
