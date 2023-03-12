# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        q = collections.deque()
        q.append(root)

        while q:
            qLen = len(q)
            level = []
            for i in range(qLen):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                res.append(level)
        
        return res
    

# #  LIST WAY
# root = [3,9,20,None,None,15,7]
# rootLen = len(root) 
# queue, res  = [0], []

# while queue:
#     qLen = len(queue)
#     level = []
#     for i in range(qLen):
#         idx = queue.pop(0)

#         if root[idx]:
#             level.append(root[idx])
#             if 2*idx+1 < rootLen: queue.append(2*idx+1)
#             if 2*idx+2 < rootLen: queue.append(2*idx+2)

#     res.append(level)
    
# print(res)