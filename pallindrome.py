#  here we will create pallindrome program without using builtin function.

class Solution:
    def isPalindrome(self, s :str) -> bool:
        length = 0
        for _ in s:
            length += 1
        
        l , r = 0, length-1

        while l < r:
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True

c1 = Solution()
print(c1.isPalindrome("ABABA"))
print(c1.isPalindrome("ABBA"))
print(c1.isPalindrome("ABCD"))        
