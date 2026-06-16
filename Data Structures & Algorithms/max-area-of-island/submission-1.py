class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxIslands=0
        m,n=len(grid),len(grid[0])
        visit=set()
        def dfs(i,j):
            if (i<0 or i>=m or j<0 or j>=n or grid[i][j]!=1 or (i,j) in visit):
                return 0
            visit.add((i,j))
            return (1 + dfs(i + 1, j) +
                        dfs(i - 1, j) +
                        dfs(i, j + 1) +
                        dfs(i, j - 1))
            


        for i in range(m):
            for j in range(n):
                num_of_islands=0
                if grid[i][j]==1:
                    maxIslands=max(maxIslands,dfs(i,j))
        return maxIslands