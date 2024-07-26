class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        row_1 = [1]
        res = [row_1]
        if numRows == 1:
            return res

        row_2 = [1,1]
        res.append(row_2)
        if numRows == 2:
            return res
        
        row_3 = [1,2,1]
        res.append(row_3)
        if numRows == 3:
            return res
        
        for n_row in range(3,numRows):
            row = []
            for i in range(n_row+1):
                if i==0 or i==n_row:
                    row.append(1)
                else:
                    val = res[n_row-1][i-1] + res[n_row-1][i]
                    row.append(val)
            res.append(row)
        return res