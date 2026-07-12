class Solution:
    def minDeletions(self, s: str) -> int:
        letter_to_freq = dict()
        for char in s:
            letter_to_freq[char] = letter_to_freq.get(char, 0) + 1
        
        freq_to_letter = dict()
        result = 0
        for letter in letter_to_freq:
            f = letter_to_freq[letter]
            freq_to_letter[f] = freq_to_letter.get(f, set())
            if len(freq_to_letter) == 0:
                freq_to_letter[f].add(letter)
            else:
                new_f = f
                while new_f > 0 and len(freq_to_letter.get(new_f, set())) > 0:
                    new_f -= 1
                
                result += f - new_f
                if new_f > 0:
                    freq_to_letter[new_f] = {letter}
        
        return result