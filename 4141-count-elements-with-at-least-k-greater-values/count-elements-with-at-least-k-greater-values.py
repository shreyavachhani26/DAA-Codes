class Solution(object):
    def countElements(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
class Solution(object):
    def countElements(self, nums, k):
        if k == 0:
            return len(nums)

        nums.sort()
        threshold = nums[-k]
        return sum(x < threshold for x in nums)
        