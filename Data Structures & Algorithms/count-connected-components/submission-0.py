class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        d=defaultdict(list)
        res=0
        for u,v in edges:
            d[u].append(v)
            d[v].append(u)
        visit=[False]*n
        def dfs(node):
            for nei in d[node]:
                if not visit[nei]:
                    visit[nei]=True
                    dfs(nei)
        
        for k in range(n):
            if not visit[k]:
                visit[k]=True
                dfs(k)
                res+=1
        return res

        