class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        q=deque()
        output=[]

        l,r=0,0

        while r < len(nums):

            #Remove small elements before inserting

            while q and nums[r]>nums[q[-1]]:
                q.pop()
            q.append(r)

            if l> q[0]:
                q.popleft()
                
            
            if r>=k-1:
                output.append(nums[q[0]])
                l+=1
            r+=1

        return output