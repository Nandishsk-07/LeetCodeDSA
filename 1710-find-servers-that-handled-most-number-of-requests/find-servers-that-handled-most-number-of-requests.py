class FenwickTree(object):
    def __init__(self, size):
        self.size = size
        self.tree = [0] * (size + 1)
    def add(self, idx, delta):
        i = idx + 1
        while i <= self.size:
            self.tree[i] += delta
            i += i & -i        
    def query(self, idx):
        s = 0
        i = idx + 1
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s
    def find_first_ge(self, target):
        """Find the smallest index >= target with value 1."""
        prefix_before = self.query(target - 1) if target > 0 else 0
        total_after = self.query(self.size - 1)
        if total_after - prefix_before > 0:
            k = prefix_before + 1
        elif prefix_before > 0:
            k = 1
        else:
            return -1
        idx = 0
        bit_mask = 1 << (self.size.bit_length() - 1)
        while bit_mask > 0:
            next_idx = idx + bit_mask
            if next_idx <= self.size and self.tree[next_idx] < k:
                idx = next_idx
                k -= self.tree[idx]
            bit_mask >>= 1
        return idx  # 0-indexed
class Solution(object):
    def busiestServers(self, k, arrival, load):
        """
        :type k: int
        :type arrival: List[int]
        :type load: List[int]
        :rtype: List[int]
        """
        bit = FenwickTree(k)
        for i in xrange(k):
            bit.add(i, 1)
        busy = [] 
        request_count = [0] * k
        for i in xrange(len(arrival)):
            arr = arrival[i]
            dur = load[i]
            while busy and busy[0][0] <= arr:
                free_time, server_id = heapq.heappop(busy)
                bit.add(server_id, 1)
            target = i % k
            chosen_server = bit.find_first_ge(target)
            if chosen_server == -1:
                continue
            bit.add(chosen_server, -1)
            request_count[chosen_server] += 1
            heapq.heappush(busy, (arr + dur, chosen_server))
        max_requests = max(request_count)
        return [i for i in xrange(k) if request_count[i] == max_requests]
        