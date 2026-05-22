class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map={}
        for num in nums:
            if num in map:
                map[num] = map.get(num, 0)+1
            else:
                map[num] = 1
        items = map.items()
        sorted_items = sorted(items, key= lambda pair: pair[1], reverse=True)

        ans = []
        topk=sorted_items[:k]

        for pair in topk:
            ans.append(pair[0])
        return ans