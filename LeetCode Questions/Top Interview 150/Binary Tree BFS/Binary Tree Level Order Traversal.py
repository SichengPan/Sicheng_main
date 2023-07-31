import collections

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
                    for example: TreeNode{val: 3, left: TreeNode{val: 9, left: None, right: None}, right: TreeNode{val: 20, left: TreeNode{val: 15, left: None, right: None}, right: TreeNode{val: 7, left: None, right: None}}}
        :rtype: List[List[int]]
                    for example: [[3],[9,20],[15,7]]
        """
        return_tree = []

        if (not root): # check if the root is empty, if it is, return []
            return return_tree
        else: # check if the root is empty, if it is not, do the follows
            # append the entire tree into the deque() structure
            tree = collections.deque() # create a deque(), this is similar to a list and can do append, appendleft, pop, popleft
            tree.append(root)

            while (tree):
                tree_level = []
                for i in range(len(tree)):
                    # pop out the first layer node of the current deque structure
                    # actually, the deque structure is like:
                    # deque([TreeNode{val: 3, left: TreeNode{val: 9, left: None, right: None}, right: TreeNode{val: 20, left: TreeNode{val: 15, left: None, right: None}, right: TreeNode{val: 7, left: None, right: None}}}]
                    # So when the first is poped out, we pop out the entire tree
                    node = tree.popleft()  
                    tree_level.append(node.val)  # put that node into the list 
                    
                    # So if there's something be the left node or right node of the first node, it needs to be inserted back, or we only get the first node
                    if (node.left):
                        tree.append(node.left)
                    if (node.right):
                        tree.append(node.right) 

                return_tree.append(tree_level)
            return return_tree  

class TreeNode:
    # Python has no built-in TreeNode, needs to define it ourselves
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


if __name__ == "__main__":
    # Create the given tree [3,9,20,null,null,15,7]
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    # Create the Solution instance
    solution = Solution()

    # Call the levelOrder method
    result = solution.levelOrder(root)
    print(result)
            