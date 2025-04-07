class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        low, high = 0, (m*n)-1

        while low <= high:
            mid = low + (high - low) // 2
            mmid = (mid//n, mid%n)
            if matrix[mmid[0]][mmid[1]] == target:
                return True
            if target < matrix[mmid[0]][mmid[1]]:
                high = mid - 1
            else:
                low = mid + 1
        
        return False