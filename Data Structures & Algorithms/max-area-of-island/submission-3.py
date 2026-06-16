class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        matrix={}
        
        maxArea=0
        visited=[]
        m,n=len(grid),len(grid[0])
        def dfs(i,j):
            if i<0 or i==m or j<0 or j>=n or grid[i][j]==0 or (i,j) in visited:
                return 0
            visited.append((i,j))
            return 1+dfs(i,j+1)+dfs(i,j-1)+dfs(i-1,j)+dfs(i+1,j)





        

        for i in range(m):
            for j in range(n):

                area=dfs(i,j)
                maxArea=max(area,maxArea)
        
        return maxArea