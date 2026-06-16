class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        visited=set()
        rows=len(board)
        cols=len(board[0])

        def dfs(r,c,cnt):
            if cnt==len(word):
                return True
            
            if r>=rows or c>=cols or r<0 or c<0 or board[r][c]!=word[cnt] or (r,c) in visited:
                return False
            
            visited.add((r,c))

            res = dfs(r+1,c,cnt+1) or dfs(r-1,c,cnt+1) or dfs(r,c+1,cnt+1) or dfs(r,c-1,cnt+1)

            visited.remove((r,c))
            return res
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c]==word[0]:
                    if dfs(r,c,0):
                        return True
        
        return False