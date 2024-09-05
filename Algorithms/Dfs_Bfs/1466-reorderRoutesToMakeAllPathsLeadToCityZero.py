class Solution(object):
    def minReorder(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        self.edges = {(a, b) for a, b in connections}
        neighbors = {city: [] for city in range(n)}
        self.visited = set()
        self.changes = 0

        for a, b in connections:
            neighbors[a].append(b)
            neighbors[b].append(a)

        # Add city 0 to visited before starting the DFS
        self.visited.add(0)
        self.dfs(0, neighbors)
        return self.changes
        
    def dfs(self, city, neighbors):
        for neighbor in neighbors[city]:
            if neighbor in self.visited:
                continue
            # Check if this neighbor can reach city 0
            if (neighbor, city) not in self.edges:
                self.changes += 1
            self.visited.add(neighbor)
            self.dfs(neighbor, neighbors)
