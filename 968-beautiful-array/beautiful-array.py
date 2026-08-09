class Solution(object):
    def beautifulArray(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
class Solution(object):
    def beautifulArray(self, n):
        arr = [1]
        while len(arr) < n:
            arr = [2 * x - 1 for x in arr] + [2 * x for x in arr]
            arr = [x for x in arr if x <= n]
        return arr