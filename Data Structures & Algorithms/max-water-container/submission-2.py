class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea=0

        i,j=0,len(heights)-1

        while i<j:
            currMin=min(heights[i],heights[j])
            maxArea=max(maxArea,currMin*(j-i))

            if (heights[i]<=heights[j]):
                i+=1
            else:
                j-=1

        return maxArea
        