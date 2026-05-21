class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap ={}
# [1,2,3,4], 7 ,,6
        # for i in range(0, len(nums)):
        #     need = target-nums[i]
        #     if need in prevMap:
        #         return [prevMap[need], i]
        #     prevMap[nums[i]]=i
        # return
        map ={}
        for i in range(len(nums)):
            diff=target-nums[i]
            if diff in map:
                return [map[diff], i]
            map[nums[i]]=i


