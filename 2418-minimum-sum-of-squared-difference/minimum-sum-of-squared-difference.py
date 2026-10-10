class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        k = k1 + k2
        max_diff = 0
        diffs = []
        for a, b in zip(nums1, nums2):
            d = abs(a - b)
            diffs.append(d)
            if d > max_diff:
                max_diff = d
        if sum(diffs) <= k:
            return 0
        count = [0] * (max_diff + 1)
        for d in diffs:
            count[d] += 1
        for d in range(max_diff, 0, -1):
            if count[d] == 0:
                continue
            if k >= count[d]:
                k -= count[d]
                count[d - 1] += count[d]
                count[d] = 0
            else:
                count[d] -= k
                count[d - 1] += k
                k = 0
                break
        return sum(d * d * count[d] for d in range(1, max_diff + 1))
        