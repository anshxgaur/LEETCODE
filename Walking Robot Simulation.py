class Solution:
    def robotSim(self, commands: list[int], obstacles: list[list[int]]) -> int:
        # Directions in clockwise order: North, East, South, West
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        dir_idx = 0  # Starts facing North
        
        x, y = 0, 0
        max_dist_sq = 0
        
        # Convert obstacles to a set of tuples for O(1) lookups
        obstacle_set = set((obs[0], obs[1]) for obs in obstacles)
        
        for cmd in commands:
            if cmd == -2:
                # Turn left 90 degrees
                dir_idx = (dir_idx - 1) % 4
            elif cmd == -1:
                # Turn right 90 degrees
                dir_idx = (dir_idx + 1) % 4
            else:
                # Move forward `cmd` steps
                dx, dy = directions[dir_idx]
                for _ in range(cmd):
                    # Check if the next step is an obstacle
                    if (x + dx, y + dy) not in obstacle_set:
                        x += dx
                        y += dy
                        # Update the maximum distance squared
                        max_dist_sq = max(max_dist_sq, x*x + y*y)
                    else:
                        # Hit an obstacle, stop moving for this command
                        break
                        
        return max_dist_sq
