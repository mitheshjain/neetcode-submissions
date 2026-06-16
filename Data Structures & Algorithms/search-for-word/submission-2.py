class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        visited=set()
        m,n =len(board),len(board[0])

        def dfs(i,j,cnt):
            if cnt==len(word):
                return True
            if i>=m or j>=n or i<0 or j<0 or board[i][j]!=word[cnt] or (i,j) in visited:
                return False
            
            visited.add((i,j))
            cnt+=1

            res=dfs(i+1,j,cnt) or dfs(i,j+1,cnt) or dfs(i-1,j,cnt) or dfs(i,j-1,cnt)
            visited.remove((i,j))
            return res



        for i in range(m):
            for j in range(n):
                if board[i][j]==word[0]:
                    if dfs(i,j,0):
                        return True
        return False