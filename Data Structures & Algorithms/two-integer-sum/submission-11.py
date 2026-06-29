class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        for i in range(len(nums)):
            n=nums[i]
            if(target-n) not in h:
                h[n]=i 
            else:
                return [h[target-n],i]
