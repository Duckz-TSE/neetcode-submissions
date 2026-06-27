class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        start = 0
        s = ''.join(c.lower() for c in s if c.isalnum())
        end = len(s) - 1
        for start in range(len(s) // 2):
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True