class Solution(object):
    def countNonDecreasingSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        ans = 0
        ops = 0
        r = n - 1
        dq = deque()
        for l in xrange(n - 1, -1, -1):
            curr_val = nums[l]
            curr_count = 1
            while dq and dq[0][0] <= curr_val:
                val, cnt = dq.popleft()
                ops += (curr_val - val) * cnt
                curr_count += cnt
            dq.appendleft([curr_val, curr_count])
            while ops > k:
                ops -= dq[-1][0] - nums[r]
                dq[-1][1] -= 1
                if dq[-1][1] == 0:
                    dq.pop()
                r -= 1
            ans += r - l + 1
        return ans
                
        