
## Works fine but slow
# class Solution:
#     def lengthOfLastWord(self, s: str) -> int:
#         return len(s.strip().split()[-1])

## Faster by ~ 50%
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        for i in range(len(s)-1,-1,-1):
            if s[i] != " ":
                length += 1
                continue
            if s[i] == " " and length == 0:
                continue
            break
            
        return length

if __name__ == "__main__":
    print(Solution().lengthOfLastWord("   fly me   to   the moon  "))