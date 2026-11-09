class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        available = SortedList(range(k))
        busy = []
        request_count = [0] * k
        for i, (arr, dur) in enumerate(zip(arrival, load)):
            while busy and busy[0][0] <= arr:
                _, server_id = heapq.heappop(busy)
                available.add(server_id)
            if not available:
                continue
            target = i % k
            idx = available.bisect_left(target)
            if idx == len(available):
                idx = 0
            chosen_server = available.pop(idx)
            request_count[chosen_server] += 1
            heapq.heappush(busy, (arr + dur, chosen_server))
        max_requests = max(request_count)
        return [i for i, count in enumerate(request_count) if count == max_requests]
        