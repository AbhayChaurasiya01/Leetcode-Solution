class Solution(object):

    def minMoves(self, classroom, energy):
        """
        :type classroom: List[str]
        :type energy: int
        :rtype: int
        """
        from collections import deque

        m = len(classroom)
        n = len(classroom[0])

        litter_id = [[-1] * n for _ in range(m)]
        sx = sy = 0
        count = 0

        for i in range(m):
            for j in range(n):
                if classroom[i][j] == 'S':
                    sx, sy = i, j
                elif classroom[i][j] == 'L':
                    litter_id[i][j] = count
                    count += 1

        if count == 0:
            return 0

        full_mask = (1 << count) - 1
        mask_count = 1 << count

        # (position, mask) -> maximum energy
        best = {}

        start_key = (sx * n + sy) * mask_count + full_mask
        best[start_key] = energy

        q = deque()
        q.append((sx, sy, energy, full_mask))

        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]

        moves = 0

        while q:

            for _ in range(len(q)):
                x, y, e, mask = q.popleft()

                if mask == 0:
                    return moves

                if e == 0:
                    continue

                for dx, dy in directions:
                    nx = x + dx
                    ny = y + dy

                    if nx < 0 or nx >= m or ny < 0 or ny >= n:
                        continue

                    if classroom[nx][ny] == 'X':
                        continue

                    ne = e - 1
                    nmask = mask

                    # Collect litter
                    if classroom[nx][ny] == 'L':
                        idx = litter_id[nx][ny]
                        nmask &= ~(1 << idx)

                    # Recharge energy
                    if classroom[nx][ny] == 'R':
                        ne = energy

                    if nmask == 0:
                        return moves + 1

                    key = (nx * n + ny) * mask_count + nmask

                    # Keep only the state with maximum energy
                    if ne > best.get(key, -1):
                        best[key] = ne
                        q.append((nx, ny, ne, nmask))

            moves += 1

        return -1