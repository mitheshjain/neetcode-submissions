class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        d=defaultdict(list)
        res=0
        for u,v in edges:
            d[u].append(v)
            d[v].append(u)
        visit=[False]*n
        

        def bfs(node):
            q=deque([node])
            visit[node]=True
            while q:
                curr=q.popleft()
                for nei in d[curr]:
                    if not visit[nei]:
                        visit[nei]=True
                        q.append(nei)
        for k in range(n):
            if not visit[k]:
                bfs(k)
                res+=1
        return res

        