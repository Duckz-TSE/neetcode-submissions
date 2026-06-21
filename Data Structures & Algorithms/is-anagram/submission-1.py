class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter
        map1 = Counter(s)
        map2 = Counter(t)

        if map2 == map1:
            return True
        return False