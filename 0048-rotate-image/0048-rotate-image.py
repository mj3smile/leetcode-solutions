class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        n = len(matrix)
        top, bottom, left, right = 0, n - 1, 0, n - 1

        for _ in range(n // 2):
            rightSide = matrix[top][left:right+1]
            leftSide = matrix[bottom][left:right+1]
            topSide = list()
            bottomSide = list()
            for i in range(top, bottom + 1):
                topSide.append(matrix[i][left])
                bottomSide.append(matrix[i][right])
            topSide = topSide[::-1]
            bottomSide = bottomSide[::-1]

            counter = 0
            for i in range(left, right + 1):
                matrix[top][i] = topSide[counter]
                matrix[bottom][i] = bottomSide[counter]
                matrix[i][left] = leftSide[counter]
                matrix[i][right] = rightSide[counter]
                counter += 1
            
            top += 1
            left += 1
            bottom -= 1
            right -= 1
