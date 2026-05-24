class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap={}
        for num in nums:
            hmap[num] = hmap.get(num, 0)+1
        items = hmap.items()
        sorted_items = sorted(items, key= lambda pair:pair[1], reverse=True)

        topk = sorted_items[:k]
        ans = []
        for pair in topk:
            ans.append(pair[0])
        return ans

        