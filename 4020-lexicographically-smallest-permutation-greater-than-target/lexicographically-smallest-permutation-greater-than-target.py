class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n = len(s)
        total_count = Counter(s)
        prefix_counts = [Counter()]
        for i in range(n):
            curr = prefix_counts[-1].copy()
            curr[target[i]] += 1
            prefix_counts.append(curr)
        for i in range(n - 1, -1, -1):
            req_prefix = prefix_counts[i]
            if any(req_prefix[ch] > total_count[ch] for ch in req_prefix):
                continue
            rem_count = total_count - req_prefix
            target_char = target[i]
            chosen_char = None
            for code in range(ord(target_char) + 1, ord('z') + 1):
                ch = chr(code)
                if rem_count[ch] > 0:
                    chosen_char = ch
                    break      
            if chosen_char is not None:
                rem_count[chosen_char] -= 1
                suffix = []
                for code in range(ord('a'), ord('z') + 1):
                    ch = chr(code)
                    if rem_count[ch] > 0:
                        suffix.append(ch * rem_count[ch])
                return target[:i] + chosen_char + "".join(suffix)
        return ""
        