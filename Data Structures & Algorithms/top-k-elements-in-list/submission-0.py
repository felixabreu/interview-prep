class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numFrequency, buckets = dict(), dict()

        for num in nums:
            #.get sets default value if key hasn't been set yet
            numFrequency[num] = numFrequency.get(num, 0) + 1
            count = numFrequency[num]
            # .setdefault does same as .get in this case
            buckets.setdefault(count, []).append(num)
        
        answer = []
        for i in range(len(nums), 0, -1):
            for num in buckets.get(i, []):
                if num not in answer:
                    answer.append(num)
                if len(answer) == k:
                    return answer
        return answer