from collections import deque

class Solution:
    def minMoves(self, classroom, energy):
        m, n = len(classroom), len(classroom[0])
        start = None
        litter_positions = []
        for r in range(m):
            for c in range(n):
                cell = classroom[r][c]
                if cell == 'S':
                    start = (r, c)
                elif cell == 'L':
                    litter_positions.append((r, c))
                    
        num_litters = len(litter_positions)
        target_mask = (1 << num_litters) - 1
        if num_litters == 0:
            return 0
        litter_idx = {pos: i for i, pos in enumerate(litter_positions)}
        max_energy_seen = [
            [[-1] * (1 << num_litters) for _ in range(n)]
            for _ in range(m)
        ]
        
        sr, sc = start
        initial_mask = 0
        initial_energy = energy
        queue = deque([(0, sr, sc, initial_mask, initial_energy)])
        max_energy_seen[sr][sc][initial_mask] = initial_energy
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        while queue:
            moves, r, c, mask, cur_energy = queue.popleft()
            if cur_energy < max_energy_seen[r][c][mask]:
                continue
                
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and classroom[nr][nc] != 'X':
                    next_energy = cur_energy - 1
                    
                    if next_energy < 0:
                        continue
                    
                    cell = classroom[nr][nc]
                    next_mask = mask
                    if (nr, nc) in litter_idx:
                        next_mask |= (1 << litter_idx[(nr, nc)])
                    if next_mask == target_mask:
                        return moves + 1
                    if cell == 'R':
                        next_energy = energy
                    if next_energy > 0:
                        if next_energy > max_energy_seen[nr][nc][next_mask]:
                            max_energy_seen[nr][nc][next_mask] = next_energy
                            queue.append((moves + 1, nr, nc, next_mask, next_energy))
                            
        return -1