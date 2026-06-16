class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        m={}
        left=0
        res=0
        for right,char in enumerate(s):
            if s[right] in m:
                left=max(left,m[char]+1)
            m[char]=right
            res=max(res,right-left+1)
        return res
