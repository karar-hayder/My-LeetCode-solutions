from typing import List

### Works but not efficient
# class Solution:
#     def twoSum(self, nums: list[int], target: int) -> list[int]:
#         i,j = 0,1
#         while i < len(nums):
#             while j < len(nums):
#                 if j == i:
#                     continue
#                 if nums[i] + nums[j] == target:
#                     return [i,j]
#                 j += 1
#             i += 1
#             j = i + 1
#         return -1

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_index = {}
        for ind,num in enumerate(nums):
            needed = target - num
            if needed in num_index:
                return [num_index[needed],ind]
            num_index[num] = ind


if __name__ == "__main__":
    print(Solution().twoSum([3,3],6))