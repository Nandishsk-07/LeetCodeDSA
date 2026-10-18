class Solution:
    def numOfWays(self, nums: list[int]) -> int:
        MOD = 1_000_000_007
        def ways(arr: list[int]) -> int:
            if len(arr) <= 2:
                return 1
            root = arr[0]
            left = [x for x in arr[1:] if x < root]
            right = [x for x in arr[1:] if x > root]
            comb = math.comb(len(left) + len(right), len(left)) % MOD
            return (comb * ways(left) % MOD * ways(right)) % MOD
        return (ways(nums) - 1) % MOD
        