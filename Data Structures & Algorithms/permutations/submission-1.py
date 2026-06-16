class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result=[]
        def dfs(curr):

            if len(curr)==len(nums):
                result.append(curr.copy())
                return
            for n in nums:
                if n not in curr:
                    curr.append(n)
                    dfs(curr)
                    curr.pop()

        dfs([])

        return result
            