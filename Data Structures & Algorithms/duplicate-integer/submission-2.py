class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap={}
        # count=0
        # 1,2,3,3
        # 0-> 1, 
        for i in range(len(nums)):
            if nums[i] in hashmap:
                return True
            hashmap[nums[i]]=0
        return False
        