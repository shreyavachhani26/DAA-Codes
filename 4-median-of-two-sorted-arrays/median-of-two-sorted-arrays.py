class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        left, right = 0, m
        half = (m + n + 1) // 2

        while left <= right:
            i = (left + right) // 2
            j = half - i

            a = nums1[i - 1] if i > 0 else float('-inf')
            b = nums1[i] if i < m else float('inf')
            c = nums2[j - 1] if j > 0 else float('-inf')
            d = nums2[j] if j < n else float('inf')

            if a <= d and c <= b:
                if (m + n) % 2:
                    return float(max(a, c))
                return (max(a, c) + min(b, d)) / 2.0

            if a > d:
                right = i - 1
            else:
                left = i + 1