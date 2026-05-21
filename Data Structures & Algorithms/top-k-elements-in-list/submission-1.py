class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h={}
        for i in range(len(nums)):
            h[nums[i]]=h.get(nums[i],0)+1
        items = h.items()
        sorted_items = sorted(items, key=lambda p : p[1], reverse=True)
        top_k= sorted_items[:k]
        ans=[]
        for pair in top_k:
            ans.append(pair[0])
        return ans