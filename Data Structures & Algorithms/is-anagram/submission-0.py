class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        table1 = {}
        table2 = {}
        
        for ch in s:
            table1[ch] = table1.get(ch, 0) + 1
        for ch in t:
            table2[ch] = table2.get(ch, 0) + 1

        if table1 == table2:
            return True
        return False