from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]: 
        res = []
        hashmap = {}

        for s in strs:
            temp = "".join(sorted(s))

            if temp not in hashmap.keys():
                hashmap[temp] = []

            hashmap[temp].append(s)

        for key , value in hashmap.items():
            res.append(value)

        return res


c1 = Solution()
print(c1.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])) 

   


        