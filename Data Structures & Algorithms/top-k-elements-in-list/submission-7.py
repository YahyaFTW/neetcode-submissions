class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap={}
        for num in nums:
            hmap[num] = hmap.get(num, 0)+1
        items = hmap.items()
        sorted_items = sorted(items, key= lambda pair:pair[1], reverse=True)

        # topk = 
        return [pair[0] for pair in sorted_items[:k]]
        
        # return ans

        