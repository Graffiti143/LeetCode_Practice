class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        import copy
        up_matrix = copy.deepcopy(matrix)

        i_pos = set()
        j_pos = set()

        row_0 = [0] * len(matrix[0])
        matrix_0 = [row_0] * len(matrix)

        for row_i in range(len(up_matrix)):
            col_j = [i for i,x in enumerate(up_matrix[row_i]) if x==0]
            if len(col_j) > 0:
                j_pos = j_pos.union(set(col_j))
                matrix[row_i] = row_0
                
        if matrix_0 != matrix:
            for j in j_pos:
                for i in range(len(up_matrix)):
                    matrix[i][j] = 0
        




