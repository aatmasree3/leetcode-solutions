# Definition for a Node.
class Node(object):
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        oldToNew = {}  # Dictionary to map original nodes to their clones

        def dfs(node):
            if node in oldToNew:  # If the node is already copied, return its clone
                return oldToNew[node]

            # Create a new node for the current node
            copy = Node(node.val)
            oldToNew[node] = copy  # Map the original node to the new node

            # Recursively copy all the neighbors
            for nei in node.neighbors:  # Corrected spelling of 'neighbors'
                copy.neighbors.append(dfs(nei))  # Corrected spelling of 'neighbors'

            return copy  # Return the cloned node

        return dfs(node) if node else None  # Start the DFS from the input node if it's not None
