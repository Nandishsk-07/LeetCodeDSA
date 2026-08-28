class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)
        counts = Counter(s)
        odd_chars = [ch for ch, freq in counts.items() if freq % 2 != 0]
        if len(odd_chars) > 1:
            return ""    
        mid_char = odd_chars[0] if odd_chars else ""
        half_counts = Counter({ch: freq // 2 for ch, freq in counts.items()})
        m = n // 2   
        candidates = []
        target_half = target[:m]
        target_counts = Counter(target_half)
        if all(half_counts[ch] >= target_counts[ch] for ch in target_counts):
            rem = half_counts - target_counts
            suffix = "".join(ch * rem[ch] for ch in sorted(rem.keys()))
            first_half = target_half + suffix
            pal = first_half + mid_char + first_half[::-1]
            if pal > target:
                candidates.append(pal)
        prefix_counts = Counter()
        for i in range(m):
            t_char = target[i]
            for code in range(ord(t_char) + 1, ord('z') + 1):
                c = chr(code)
                if half_counts[c] > prefix_counts[c]:
                    rem = half_counts - prefix_counts
                    rem[c] -= 1
                    rest = "".join(ch * rem[ch] for ch in sorted(rem.keys()))
                    first_half = target[:i] + c + rest
                    pal = first_half + mid_char + first_half[::-1]
                    if pal > target:
                        candidates.append(pal)
                    break          
            prefix_counts[t_char] += 1
            if prefix_counts[t_char] > half_counts[t_char]:
                break  
        return min(candidates) if candidates else ""
        