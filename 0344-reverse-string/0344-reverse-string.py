class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for left in range(len(s)//2):
            right = len(s) - left - 1
            s[left], s[right] = s[right], s[left]