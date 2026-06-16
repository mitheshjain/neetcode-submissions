class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        r,c=len(grid),len(grid[0])
        visit=set()
        q=deque()
        distance=0


        for m in range(r):
            for n in range(c):
                if grid[m][n]==0:
                    q.append([m,n])
                    visit.add((m,n))
        def addRoom(i,j):
            if i<0 or i==r or j<0 or j==c or (i,j) in visit or grid[i][j]==-1:
                return
            q.append([i,j])
            visit.add((i,j))
        

        while q:
            for i in range(len(q)):
                a,b=q.popleft()
                grid[a][b]=distance
                addRoom(a,b+1)
                addRoom(a,b-1)
                addRoom(a+1,b)
                addRoom(a-1,b)

            distance+=1    
          
