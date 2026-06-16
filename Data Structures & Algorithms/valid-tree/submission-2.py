class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        d=defaultdict(list)

        for u,v in edges:
            d[u].append(v)
            d[v].append(u)
        
        visited=set()

        def dfs(node,parent):
            if node in visited:
                return False
            visited.add(node)
            for nei in d[node]:
                if nei==parent:
                    continue
                
                if not dfs(nei,node):
                    return False

            return True
        return dfs(0,-1) and n==len(visited)