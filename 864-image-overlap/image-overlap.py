class Solution(object):
    def largestOverlap(self, img1, img2):
        """
        :type img1: List[List[int]]
        :type img2: List[List[int]]
        :rtype: int
        """
        n = len(img1)
        ones1 = [(r, c) for r in xrange(n) for c in xrange(n) if img1[r][c] == 1]
        ones2 = [(r, c) for r in xrange(n) for c in xrange(n) if img2[r][c] == 1]
        if not ones1 or not ones2:
            return 0
        shift_counts = Counter()
        for r1, c1 in ones1:
            for r2, c2 in ones2:
                shift_counts[(r2 - r1, c2 - c1)] += 1
        return max(shift_counts.values())
        