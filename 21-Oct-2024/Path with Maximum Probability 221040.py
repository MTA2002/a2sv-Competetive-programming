# Problem: Path with Maximum Probability - https://leetcode.com/problems/path-with-maximum-probability/

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = defaultdict(list)

        for i in range(len(edges)):
            u, v = edges[i]
            w = succProb[i]
            graph[u].append((v, w))
            graph[v].append((u, w))

        probs = [0] * n
        probs[start_node] = 1
        visited = set()

        heap = [(-1, start_node)]

        while heap:
            cur_prob, cur_node = heappop(heap)
            cur_prob *= -1

            if cur_node in visited:
                continue
            
            visited.add(cur_node)

            for neighbor, probability in graph[cur_node]:
                prob = cur_prob * probability

                if prob > probs[neighbor]:
                    probs[neighbor] = prob
                    heappush(heap, (-prob, neighbor))
        
        return probs[end_node]