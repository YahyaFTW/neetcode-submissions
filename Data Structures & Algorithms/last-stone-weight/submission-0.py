class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        import heapq
        if(len(stones)==1):
            return stones[0]
        
        heap = []
        # [2,3,6,2,4]
        for i in range(len(stones)):
            heapq.heappush(heap, -stones[i])
        # [1]

        for i in range(len(heap)):
            if(len(heap)>1):
                s1 = heapq.heappop(heap)
                s2 = heapq.heappop(heap)
                n= s1-s2
                if (n!=0):
                    heapq.heappush(heap, -abs(n))
        if len(heap)==1:
            return -heap[0]
        else:
            return 0


