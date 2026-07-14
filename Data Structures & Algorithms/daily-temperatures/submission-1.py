class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        left, right, res = 0, 1, [0]* len(temperatures)

        while right < len(temperatures):
            if temperatures[left] < temperatures [right]:
                res[left] = right - left
                left +=1
                right = left + 1
            #case when there isnt a temperatur higher 
            elif left < len(temperatures) and right == len(temperatures)-1:
                left += 1
                right = left + 1
            else:
                right += 1

        return res 

