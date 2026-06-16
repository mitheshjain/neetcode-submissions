class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        result=0
        maxHeap=[]

        for val in nums:
          heapq.heappush(maxHeap,-val)

        for i in range(k):
          result=heapq.heappop(maxHeap)

        return -result