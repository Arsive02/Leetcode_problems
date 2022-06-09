class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        k = list(zip(*matrix))
        l = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == min(matrix[i]) and matrix[i][j] == max(k[j]):
                    l.append(matrix[i][j])
        return l
