class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        l,maxLen=0,0
        t={}
        for r in range(len(s)):
            if s[r]  in t:
                l=max(t[s[r]]+1,l)
            t[s[r]] =r
            maxLen=max(maxLen,r-l+1)
        return maxLen