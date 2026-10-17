class Solution(object):
    def minSwaps(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        def get_digit_sum(x):
            s = 0
            while x > 0:
                s += x % 10
                x //= 10
            return s
        items = [(get_digit_sum(nums[i]), nums[i], i) for i in xrange(n)]
        items.sort()
        visited = [False] * n
        swaps = 0
        for i in xrange(n):
            if visited[i] or items[i][2] == i:
                continue
            cycle_len = 0
            curr = i
            while not visited[curr]:
                visited[curr] = True
                curr = items[curr][2]
                cycle_len += 1
            if cycle_len > 1:
                swaps += cycle_len - 1
        return swaps 
        