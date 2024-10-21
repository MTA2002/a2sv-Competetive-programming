# Problem: Design Graph With Shortest Path Calculator - https://leetcode.com/problems/design-graph-with-shortest-path-calculator/

class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.n = n
        self.graph = defaultdict(list)

        for u, v, w in edges:
            self.graph[u].append((v, w))

    def addEdge(self, edge: List[int]) -> None:
        u, v, w = edge
        self.graph[u].append((v, w))
        

    def shortestPath(self, node1: int, node2: int) -> int:
        dists = [inf] * self.n
        dists[node1] = 0
        heap = [(0, node1)]
        visited = set()

        while heap:
            cur_dist, cur_node = heapq.heappop(heap)

            if cur_node in visited:
                continue
            
            visited.add(cur_node)

            for neighbor , weight in self.graph[cur_node]:
                distance = weight + cur_dist

                if distance < dists[neighbor]:
                    dists[neighbor] = distance
                    heapq.heappush(heap, (distance, neighbor))
        
        return dists[node2] if dists[node2] != inf else -1

                    

        


# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)