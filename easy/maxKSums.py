from typing import List


class Solution:

    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()

        i = 0
        j = len(nums) - 1
        ct = 0

        while i < j:
            temp_sum = nums[i] + nums[j]
            if temp_sum == k:
                ct += 1
                i+=1
                j-=1
            elif temp_sum > k:
                j-=1
            else:
                i+=1

            
        
        return ct