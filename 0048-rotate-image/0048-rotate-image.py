class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r = len(matrix) 
       
        for x in range(r):
            for y in range(x,r):
                matrix[x][y],matrix[y][x] = matrix[y][x],matrix[x][y]

        for i in range(r):
            matrix[i].reverse()
        

        return matrix