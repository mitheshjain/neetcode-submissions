class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap=[i for i in nums[:k]]
        heapq.heapify(maxHeap)

        cnt=1

        for i in nums[k:]:
            if i > maxHeap[0]:
                heapq.heappop(maxHeap)
                heapq.heappush(maxHeap,i)
        
        return maxHeap[0]