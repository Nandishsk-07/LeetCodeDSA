class Solution(object):
    def maxNumberOfFamilies(self, n, reservedSeats):
        """
        :type n: int
        :type reservedSeats: List[List[int]]
        :rtype: int
        """
        reserved_rows = defaultdict(int)
        for r, c in reservedSeats:
            if 2 <= c <= 9:
                reserved_rows[r] |= (1 << c)       
        ans = 2 * n
        LEFT_MASK = 60
        RIGHT_MASK = 960
        MID_MASK = 240
        for mask in reserved_rows.values():
            left_open = (mask & LEFT_MASK) == 0
            right_open = (mask & RIGHT_MASK) == 0
            mid_open = (mask & MID_MASK) == 0
            if left_open and right_open:
                continue
            elif left_open or right_open or mid_open:
                ans -= 1
            else:
                ans -= 2
        return ans
        