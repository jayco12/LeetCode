class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adjacency_list = defaultdict(list)
        for src, dest in edges:
            adjacency_list[src].append(dest)
            adjacency_list[dest].append(src)  
        if source == destination:
            return True

        visited = set()
        stack = [source]

        while stack:
            node = stack.pop()
            if node == destination:
                return True
            if node not in visited:
                visited.add(node)
                stack.extend(neighbor for neighbor in adjacency_list[node] if neighbor not in visited)

        return False