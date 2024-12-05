# 199. Binary Tree Right Side View
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
from typing import Optional, List

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # If the root is None, return an empty list
        if not root:
            return []

        # Initialize the queue for level order traversal
        queue = deque([root])
        right_side_view = []

        while queue:
            # Get the number of nodes at the current level
            level_length = len(queue)
            
            # Traverse all nodes at the current level
            for i in range(level_length):
                node = queue.popleft()

                # Add the value of the rightmost node at this level to the result
                if i == level_length - 1:
                    right_side_view.append(node.val)

                # Add child nodes to the queue
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return right_side_view
