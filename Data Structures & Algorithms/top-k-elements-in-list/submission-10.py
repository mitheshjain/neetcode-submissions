class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = defaultdict(int)
        max_heap=[]
        res=[]
        for n in nums:
            hmap[n]+=1
        for n in hmap.keys():
            heapq.heappush(max_heap,(hmap[n],n))
            if len(max_heap)>k:
                heapq.heappop(max_heap)
        for i in range(k):
            res.append(heapq.heappop(max_heap)[1])
        return res