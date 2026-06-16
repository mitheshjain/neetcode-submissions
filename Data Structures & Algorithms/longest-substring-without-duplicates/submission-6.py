class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        m={}
        left=0
        maxLen=0
        for right in range(len(s)):
                if s[right] in m:
                    left = max(left,m[s[right]]+1)
                m[s[right]] = right
                maxLen=max(maxLen,right-left+1)
        return maxLen
