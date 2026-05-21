class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # mySet = set()
        
        # for i in range(len(nums)):
        #     if nums[i] in mySet:
        #         return True
        #     mySet.add(nums[i])
        # return False
        s = set()
        for num in nums:
            if num in s:
                return True
            s.add(num)
        return False
        