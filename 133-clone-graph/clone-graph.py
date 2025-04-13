"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        clones = defaultdict(Node)
        
        # BFS to store each node with it's copy
        queue = deque([node])
        seen = set()
        while queue:
            curr = queue.popleft()
            clone = Node(val=curr.val)
            clones[curr] = clone
            seen.add(curr)
            for n in curr.neighbors:
                if n not in seen:
                    queue.append(n)
        
        # Iterate through each copy to add it's neighbors
        for original, clone in clones.items():
            for n in original.neighbors:
                clone.neighbors.append(clones[n])
        
        return clones[node]