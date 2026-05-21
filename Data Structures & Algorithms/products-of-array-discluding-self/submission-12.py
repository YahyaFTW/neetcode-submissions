class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1 
        left =[1]
        right=[1]
        # [1,2,4,6]
        for i in range(1, len(nums)):
            product = product*nums[i-1]
            left.append(product)
        product=1
        for i in range(len(nums)-2, -1,-1):
            product = product*nums[i+1]
            right.append(product)
        right = right[::-1]
        ans=[]
        for i in range(0, len(nums)):
            ans.append(right[i] * left[i])
        return ans
