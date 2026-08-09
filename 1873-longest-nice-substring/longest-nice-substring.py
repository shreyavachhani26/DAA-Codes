class Solution(object):
    def longestNiceSubstring(self, s):
        """
        :type s: str
        :rtype: str
        """
class Solution(object):
    def longestNiceSubstring(self, s):
        if len(s) < 2:
            return ""

        chars = set(s)

        for i, c in enumerate(s):
            if c.lower() not in chars or c.upper() not in chars:
                left = self.longestNiceSubstring(s[:i])
                right = self.longestNiceSubstring(s[i + 1:])
                return left if len(left) >= len(right) else right

        return s