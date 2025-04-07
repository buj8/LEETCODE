class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        def mIndex(i):
            return (i//n, i%n)

        low, high = 0, (m*n)-1

        while low <= high:
            mid = low + (high - low) // 2
            mmid = mIndex(mid)
            if matrix[mmid[0]][mmid[1]] == target:
                return True
            if target < matrix[mmid[0]][mmid[1]]:
                high = mid - 1
            else:
                low = mid + 1
        
        return False