class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        out = ""
        # l = 0
        r = 0
        max_len = 0 

        while r < len(s):
            if s[r] not in out:
                out += s[r]
                max_len = max(max_len , len(out))
                r += 1

            else:
                out = out[1:]

        return max_len
    
c1 = Solution()

print(c1.lengthOfLongestSubstring("abcabcbb"))
                

