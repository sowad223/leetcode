class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        map = {mat[r][c]: (r, c) for r in range(m) for c in range(n)}
        rows, cols = [0] * m, [0] * n
        for i in range(len(arr)):
            r, c = map[arr[i]]
            rows[r] += 1
            cols[c] += 1
            if rows[r] == n or cols[c] == m:
                return i
        return -1
        