class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m, n = len(classroom), len(classroom[0])
        start_r, start_c = 0, 0
        litter_positions = {}
        for r in range(m):
            for c in range(n):
                ch = classroom[r][c]
                if ch == 'S':
                    start_r, start_c = r, c
                elif ch == 'L':
                    litter_positions[(r, c)] = len(litter_positions)           
        k = len(litter_positions)
        target_mask = (1 << k) - 1
        if target_mask == 0:
            return 0
        max_energy_left = {}
        queue = deque([(start_r, start_c, 0, energy, 0)])
        max_energy_left[(start_r, start_c, 0)] = energy
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]    
        while queue:
            r, c, mask, cur_e, moves = queue.popleft()
            if cur_e < max_energy_left.get((r, c, mask), -1):
                continue
            if cur_e == 0:
                continue    
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and classroom[nr][nc] != 'X':
                    n_energy = cur_e - 1
                    cell_type = classroom[nr][nc]
                    if cell_type == 'R':
                        n_energy = energy
                    n_mask = mask
                    if cell_type == 'L':
                        n_mask |= (1 << litter_positions[(nr, nc)])
                    if n_mask == target_mask:
                        return moves + 1
                    if n_energy > max_energy_left.get((nr, nc, n_mask), -1):
                        max_energy_left[(nr, nc, n_mask)] = n_energy
                        queue.append((nr, nc, n_mask, n_energy, moves + 1))                    
        return -1
        