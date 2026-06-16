class Solution:
    def maxArea(self, heights: List[int]) -> int:
        sum=0
        result=0
        p1=0
        p2=len(heights)-1
        while(p1<p2):
            sum = sum + min(heights[p1],heights[p2])*(p2-p1)
            if heights[p1]<heights[p2]:
                p1=p1+1
            else:
                p2=p2-1
            if result==0:
                result=sum
            else:
                result=max(result,sum)
            sum=0
        return result

