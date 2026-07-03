class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = dict()

        for i, num in enumerate(nums):
            key = target - num

            if key in numMap:
                return [min(i, numMap[key]), max(i, numMap[key])]
            
            numMap[num] = i
         