class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import heapq
        hmap={}
        for num in nums:
            hmap[num] = hmap.get(num, 0)+1
        items = hmap.items()

        heap = []
        for pair in items:

            heapq.heappush(heap, (pair[1], pair[0]))
            if(len(heap)>k):
                heapq.heappop(heap)

        return [pair[1] for pair in heap]


