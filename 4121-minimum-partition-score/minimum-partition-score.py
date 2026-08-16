class Solution(object):
    def minPartitionScore(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
class Solution(object):
    def minPartitionScore(self, nums, k):
        n = len(nums)
        prefix = [0] * (n + 1)

        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        INF = 10**30
        dp = [INF] * (n + 1)
        dp[0] = 0

        for p in range(1, k + 1):
            ndp = [INF] * (n + 1)

            def solve(l, r, optL, optR):
                if l > r:
                    return

                mid = (l + r) // 2
                best = INF
                bestPos = -1

                for j in range(optL, min(mid, optR) + 1):
                    s = prefix[mid] - prefix[j]
                    val = dp[j] + s * (s + 1) // 2

                    if val < best:
                        best = val
                        bestPos = j

                ndp[mid] = best

                solve(l, mid - 1, optL, bestPos)
                solve(mid + 1, r, bestPos, optR)

            solve(p, n, p - 1, n - 1)
            dp = ndp

        return dp[n]