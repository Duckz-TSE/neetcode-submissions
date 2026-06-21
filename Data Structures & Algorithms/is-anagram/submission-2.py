class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map1 = {}
        map2 = {}

        for letter in s:
            map1[letter] = map1.get(letter, 0) + 1
        for letter in t:
            map2[letter] = map2.get(letter, 0) + 1

        if map2 == map1:
            return True
        return False