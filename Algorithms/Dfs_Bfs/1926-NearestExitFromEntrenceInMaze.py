from collections import deque

class Solution(object):
    def nearestExit(self, maze, entrance):
        """
        :type maze: List[List[str]]
        :type entrance: List[int]
        :rtype: int
        """
        return self.bfs(maze, entrance, 0)

    def bfs(self, maze, entrance, totalMoves):
        rows = len(maze)
        columns = len(maze[0])
        visited = set()

        queue = deque([(entrance[0], entrance[1], 0)])  # (row, column, moves)

        while queue:
            row, column, moves = queue.popleft()

             # if im not the entrence and i am at the border (exit found) return the totalmoves 
            if [row, column] != entrance and (row == rows-1 or row == 0 or column == columns-1 or column == 0):
                return moves

            if (row, column) not in visited: #mark as visited
                visited.add((row, column))
    
                #check our neighbors (left, right, up, down) for next move 
                if row >0 and maze[row-1] [column] == '.': #up
                    queue.append((row - 1, column, moves + 1))

                if row < rows-1 and maze[row+1] [column] == '.': #down
                    queue.append((row + 1, column, moves + 1))

                if column >0 and maze[row] [column-1] == '.': #left
                    queue.append((row , column-1, moves + 1))

                if column < columns-1 and maze[row] [column+1] == '.': #right
                    queue.append((row, column+1, moves + 1))

        #no way to reach an exit return -1
        return -1