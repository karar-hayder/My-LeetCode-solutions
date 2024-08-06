class Solution:
    def findFinalValue(self, nums: list[int], original: int) -> int:
        res = 0 + original
        while True:
            if res in nums:
                res *= 2
                continue

            return res
        