class Solution(object):
    def assignTasks(self, servers, tasks):
        """
        :type servers: List[int]
        :type tasks: List[int]
        :rtype: List[int]
        """
        free_servers = [(servers[i], i) for i in xrange(len(servers))]
        heapq.heapify(free_servers)
        busy_servers = []
        m = len(tasks)
        ans = [0] * m
        curr_time = 0
        for j in xrange(m):
            if j > curr_time:
                curr_time = j   
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
        