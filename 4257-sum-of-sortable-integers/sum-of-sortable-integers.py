class Solution(object):
    def sortableIntegers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        is_sorted = True
        for i in xrange(1, n):
            if nums[i] < nums[i - 1]:
                is_sorted = False
                break        
        divisors = []
        d = 1
        while d * d <= n:
            if n % d == 0:
                divisors.append(d)
                if d * d != n:
                    divisors.append(n // d)
            d += 1
        if is_sorted:
            return sum(divisors)   
        def is_sortable(k):
            prev_max = -1
            for start in xrange(0, n, k):
                end = start + k
                drop_count = 0
                block_min = nums[start]
                block_max = nums[start]   
                for i in xrange(start, end - 1):
                    if nums[i] > nums[i + 1]:
                        drop_count += 1
                        if drop_count > 1:
                            return False
                    if nums[i + 1] < block_min:
                        block_min = nums[i + 1]
                    if nums[i + 1] > block_max:
                        block_max = nums[i + 1]       
                if drop_count == 1:
                    if nums[end - 1] > nums[start]:
                        return False
                if prev_max != -1 and block_min < prev_max:
                    return False
                prev_max = block_max
            return True
        total_sum = 0
        for k in divisors:
            if is_sortable(k):
                total_sum += k
        return total_sum
        