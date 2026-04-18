from typing import List

class Solutions:

    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hashmap = {}

        for i in range(len(nums)):
            hashmap[nums[i]] = i

        for i in range(len(nums)):
            compliemnt = target - nums[i]
            if compliemnt in hashmap.keys() and hashmap[compliemnt] != i:
                return [i, hashmap[compliemnt]]



        return []
    
c1 = Solutions()
print(c1.twoSum([2,7,11,15], 13))
