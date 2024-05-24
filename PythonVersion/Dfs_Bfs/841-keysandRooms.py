class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        visited = set()
        n = len(rooms)
        self.dfs(visited, 0, rooms)
       
        return len(visited) == n

    def dfs(self, visited, currentRoom, rooms):
        if currentRoom in visited:
            return 
        visited.add(currentRoom)
        for key in rooms[currentRoom]:
            self.dfs(visited, key, rooms)
