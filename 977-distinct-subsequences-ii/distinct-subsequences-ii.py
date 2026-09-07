class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 1_000_000_007
        ends_with = [0] * 26
        for ch in s:
            idx = ord(ch) - ord('a')
            ends_with[idx] = (sum(ends_with) + 1) % MOD
        return sum(ends_with) % MOD
    
        