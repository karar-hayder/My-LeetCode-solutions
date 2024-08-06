from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        ind = 1
        ## Count how many unique
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[ind] = nums[i]
                ind += 1
        return ind
