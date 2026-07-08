class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        leftPointer, rightPointer = 0, len(numbers)-1

        while(leftPointer < rightPointer):
            if numbers[leftPointer] + numbers[rightPointer] > target:
                rightPointer-=1
            elif numbers[leftPointer] + numbers[rightPointer] < target:
                leftPointer +=1
            else:
                return [min(leftPointer + 1, rightPointer + 1), max(leftPointer+1, rightPointer+1)]
