class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        finalList = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            finalList[i] = prefix
            prefix *= nums[i]
        postfix = 1
        #range is last index to -1 not inclusive, so last iteration is the 1st index of 0
        for i in range(len(nums) -1, -1, -1):
           finalList[i] *= postfix
           postfix *= nums[i]
        
        return finalList
                
                