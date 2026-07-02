import os
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common_prefix = os.path.commonprefix(strs)
        return common_prefix