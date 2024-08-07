class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        return [int(i) for i in f"{int(''.join(list(map(str,digits))))+1}"]
    
if __name__ == "__main__":
    print(Solution().plusOne([1,2,3]))