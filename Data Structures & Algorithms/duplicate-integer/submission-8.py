class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mySet =set()
        for i in range(0, len(nums)):
            if nums[i] not in mySet:
                mySet.add(nums[i])
            else:
                return True
        return False