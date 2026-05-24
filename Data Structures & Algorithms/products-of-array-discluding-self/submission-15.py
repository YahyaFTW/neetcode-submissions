class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product=1
        left=[1]
        # [1,2,4,6], [1, 1, 2, 8] 
        for i in range(1, len(nums)):
            product*=nums[i-1]
            left.append(product)

        right=[1] * len(nums)
        product=1
        # [1,1,1,1], [1,2,4,6], [48,24,6,1]
        for i in range(len(nums)-2, -1, -1):
            product*= nums[i+1]
            right[i]= product
        
        # ans=[]
        
        # for i in range(len(nums)):
        #     ans.append(right[i]*left[i])
        return [right[i]*left[i] for i in range(len(nums))]


