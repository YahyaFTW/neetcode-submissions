class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import heapq
        map = {}
        for num in nums:
            map[num]= map.get(num, 0)+1
        items = map.items()

        myheap = []
        for pair in items:
            heapq.heappush(myheap,(pair[1],pair[0]))
            if(len(myheap)>k):
                heapq.heappop(myheap)
            
        return [pair[1] for pair in myheap] 
        
        



