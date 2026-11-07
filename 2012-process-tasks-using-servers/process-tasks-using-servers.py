class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        free_servers = [(w, i) for i, w in enumerate(servers)]
        heapq.heapify(free_servers)
        busy_servers = []
        m = len(tasks)
        ans = [0] * m
        curr_time = 0
        for j in range(m):
            curr_time = max(curr_time, j)
            while busy_servers and busy_servers[0][0] <= curr_time:
                free_time, weight, index = heapq.heappop(busy_servers)
                heapq.heappush(free_servers, (weight, index))
            if not free_servers:
                curr_time = busy_servers[0][0]
                while busy_servers and busy_servers[0][0] <= curr_time:
                    free_time, weight, index = heapq.heappop(busy_servers)
                    heapq.heappush(free_servers, (weight, index))
            weight, index = heapq.heappop(free_servers)
            ans[j] = index
            heapq.heappush(busy_servers, (curr_time + tasks[j], weight, index))
        return ans
        