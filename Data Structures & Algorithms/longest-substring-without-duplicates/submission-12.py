class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        res_set=set()
        res=0
        cnt=0
        for r in range(len(s)):
            while s[r] in res_set:
                res_set.remove(s[l])
                l+=1
            res_set.add(s[r])
            res=max(res,r-l+1)
        return res