class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        path = set()
        m,n=len(board),len(board[0])
        def dfs(i,j,curr_idx):
            if curr_idx==len(word):
                return True
            if i>=m or i<0 or j>=n or j<0 or board[i][j]!=word[curr_idx] or (i,j) in path:
                return False
            
            path.add((i,j))
            curr_idx+=1
                    

            res= dfs(i+1,j,curr_idx) or  dfs(i-1,j,curr_idx) or dfs(i,j-1,curr_idx) or dfs(i,j+1,curr_idx)
            path.remove((i,j))
            return res
            
        
        for i in range(m):
            for j in range(n):
                if board[i][j]==word[0]:
                    if dfs(i,j,0):
                        return True
        
        return False