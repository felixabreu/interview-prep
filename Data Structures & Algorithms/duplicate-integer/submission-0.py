class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numMap = {}
        for index, num in enumerate(nums):
            if num in numMap:
                return True

            numMap[num] = index

        return False 
        