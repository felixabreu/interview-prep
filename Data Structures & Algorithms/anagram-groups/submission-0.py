class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strsMap = dict()
        for str in strs:
            frequencyList = [0] * 26
            for char in str:
                #ord(c) - ord('a') is a way of getting the index value of letters in the alphabet
                frequencyList[ord(char) - ord('a')] += 1
            #lists can be converted to keys for hashmaps by casting with tuple
            key = tuple(frequencyList)
            strsMap[key] = strsMap.get(key, []) + [str]
        return list(strsMap.values())