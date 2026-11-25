class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        MOD1, MOD2 = 1_000_000_007, 1_000_000_009
        BASE1, BASE2 = 131_313, 137_137
        pref1 = [0] * (n + 1)
        pref2 = [0] * (n + 1)
        pow1 = [1] * (n + 1)
        pow2 = [1] * (n + 1)
        for i in range(n):
            val = nums[i]
            pref1[i + 1] = (pref1[i] * BASE1 + val) % MOD1
            pref2[i + 1] = (pref2[i] * BASE2 + val) % MOD2
            pow1[i + 1] = (pow1[i] * BASE1) % MOD1
            pow2[i + 1] = (pow2[i] * BASE2) % MOD2
        def has_unique_of_length(L: int) -> bool:
            seen = set()
            duplicates = set()
            p1, p2 = pow1[L], pow2[L]
            for i in range(n - L + 1):
                h1 = (pref1[i + L] - pref1[i] * p1) % MOD1
                h2 = (pref2[i + L] - pref2[i] * p2) % MOD2
                key = (h1 << 32) | h2
                if key in seen:
                    duplicates.add(key)
                else:
                    seen.add(key)

            return len(seen) > len(duplicates)
        low, high = 1, n
        ans = n
        while low <= high:
            mid = (low + high) // 2
            if has_unique_of_length(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans