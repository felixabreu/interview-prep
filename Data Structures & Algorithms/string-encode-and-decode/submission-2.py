class Solution:

    def encode(self, strs: List[str]) -> str:
        finalEncode = []
        for s in strs:
            strLen = str(len(s))
            delimiter = "@"
            encodedString = strLen + delimiter + s
            finalEncode.append(encodedString)
        return "".join(finalEncode)
    def decode(self, s: str) -> List[str]:
        finalList = []
        i = 0
        while i < len(s):
            #we use two loops so we can keep track of the start, and know when we get to the end of the string
            j = i
            while s[j] != "@":
                j += 1
            stringLength = int(s[i:j])
            i = j + 1
            j = i + stringLength
            finalList.append(s[i:j])
            i = j

        return finalList
