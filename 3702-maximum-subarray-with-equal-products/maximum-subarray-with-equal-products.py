class Solution:
    def maxLength(self, nums: List[int]) -> int:
        n = len(nums)
        max_len = 1
        for i in range(n):
            prod = 1
            g = 0
            l = 1
            for j in range(i, n):
                val = nums[j]
                prod *= val
                g = math.gcd(g, val)
                l = (l * val) // math.gcd(l, val)
                if prod == l * g:
                    if j - i + 1 > max_len:
                        max_len = j - i + 1
                elif prod > l * g:
                    break
        return max_len
        