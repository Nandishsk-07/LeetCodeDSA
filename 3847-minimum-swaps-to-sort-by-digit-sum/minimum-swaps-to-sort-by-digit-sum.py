class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        def get_digit_sum(x: int) -> int:
            s = 0
            while x:
                s += x % 10
                x //= 10
            return s
        items = [(get_digit_sum(val), val, i) for i, val in enumerate(nums)]
        items.sort()
        visited = [False] * n
        swaps = 0
        for i in range(n):
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
        