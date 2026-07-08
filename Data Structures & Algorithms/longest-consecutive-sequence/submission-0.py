class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        #tracks overall longest sequence
        longest = 0
        for num in nums:
            if num - 1 not in numSet:
                #counts current sequence length
                count = 1
                num += 1
                while num in numSet:
                    count +=1
                    num +=1
                longest = max(count, longest)
        
        return longest
        