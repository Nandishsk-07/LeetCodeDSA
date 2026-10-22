class Solution:
    def minOperations(self, nums: list[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0
        p = nums.index(0)
        is_forward = True
        for i in range(n):
            if (nums[i] + 1) % n != nums[(i + 1) % n]:
                is_forward = False
                break
        if is_forward:
            if p == 0:
                return 0
            return min(p, 2 + n - p)
        is_backward = True
        for i in range(n):
            if(nums[i] - 1) % n != nums[(i + 1) % n]:
                is_backward = False
                break
        if is_backward:
            cost1 = 1 + (n - 1 - p)
            cost2 = 1 + ((p + 1) % n)
            return min(cost1, cost2)
        return -1
        