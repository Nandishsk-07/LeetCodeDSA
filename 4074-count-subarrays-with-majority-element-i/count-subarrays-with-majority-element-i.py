class Solution(object):
    def countMajoritySubarrays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        ans = 0
        for i in range(n):
            balance = 0
            for j in range(i, n):
                if nums[j] == target:
                    balance += 1
                else:
                    balance -= 1
                if balance > 0:
                    ans += 1
        return ans
        