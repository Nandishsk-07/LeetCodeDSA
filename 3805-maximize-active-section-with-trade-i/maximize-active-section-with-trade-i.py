class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        t = '1' + s + '1'
        blocks = []
        i = 0
        n = len(t)
        while i < n:
            j = i
            while j < n and t[j] == t[i]:
                j += 1
            blocks.append((t[i], j - i))
            i = j
        total_ones = s.count('1')
        max_trade_gain = 0
        for idx in range(1, len(blocks) - 1):
            if blocks[idx][0] == '1':
                if blocks[idx - 1][0] == '0' and blocks[idx + 1][0] == '0':
                    zero_gain = blocks[idx - 1][1] + blocks[idx + 1][1]
                    max_trade_gain = max(max_trade_gain, zero_gain)
                    
        return total_ones + max_trade_gain
        