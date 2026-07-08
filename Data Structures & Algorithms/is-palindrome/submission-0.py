class Solution:
    def isPalindrome(self, s: str) -> bool:
        leftPointer = 0
        rightPointer = len(s) - 1

        while leftPointer < rightPointer:
            while leftPointer < rightPointer and not self.alphaNum(s[leftPointer]):
                leftPointer+=1
            while rightPointer > leftPointer and not self.alphaNum(s[rightPointer]):
                rightPointer-=1
            
            if s[leftPointer].lower() != s[rightPointer].lower():
                return False
            leftPointer+=1
            rightPointer-=1
        return True

    #converts to lower, native
    def lowerCase(self, char: str) -> str:
        return chr(ord(char) + 32)

    def alphaNum(self, char: str) -> bool:
        return  (ord('A') <= ord(char) <= ord('Z') or
                ord('a') <= ord(char) <= ord('z') or 
                ord('0') <= ord(char) <= ord('9'))
