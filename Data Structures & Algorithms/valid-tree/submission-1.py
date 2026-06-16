class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        d=defaultdict(list)
        seen=set()
        for u,v in edges:
            d[u].append(v)
            d[v].append(u)
        def dfs(node,par):
            if node in seen:
                return False
            seen.add(node)
            for nei in d[node]:
                if nei==par:
                    continue
                if not dfs(nei,node):
                    return False
            return True

        
        return dfs(0,-1) and len(seen)==n
