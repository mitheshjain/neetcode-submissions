class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        candidates.sort()

        def dfs(start_index,curr,total):
        
            if total==target:
                res.append(list(curr))
                return
            if total>target:
                return
            
            for i in range(start_index, len(candidates)):
                if i>start_index and candidates[i-1]==candidates[i]:
                    continue
                curr.append(candidates[i])
                # We use i + 1 because each number can only be used once
                dfs(i + 1, curr, total + candidates[i])
                curr.pop() # Standard backtracking
        dfs(0,[],0)
        return res