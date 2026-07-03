class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False 
        sMap, tMap  = dict(), dict()

        for i in range(len(s)):
            char = s[i]
            tChar = t[i]

            sMap[char] = sMap.get(char, 0) + 1
            tMap[tChar] = tMap.get(tChar, 0) + 1
        return sMap == tMap        

        