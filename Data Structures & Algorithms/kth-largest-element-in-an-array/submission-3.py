class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq
        heap = []

        for i in range(len(nums)):
            num=nums[i]
            heapq.heappush(heap, num)
            if(i>=k):
                heapq.heappop(heap)

        return heap[0]