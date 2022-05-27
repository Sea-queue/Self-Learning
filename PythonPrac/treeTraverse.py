import collections
class TreeNode:
    def __init__(self, val, left=None, right=None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def inorder(self, root: TreeNode) -> list[int]:
        """ inorder: left, root, right"""

        result = list()
        if not root:
            return result
        self.inorderHelp(root, result)
        return result


    def inorderHelp(self, root: TreeNode, result: list[int]) -> None:
        if root.left:
            self.inorderHelp(root.left, result)

        result.append(root.val)

        if root.right:
            self.inorderHelp(root.right, result)


    def levelOrder_1(self, root: TreeNode) -> list[list[int]]:
        """ Level Order: from left to right, level by level """
        result = []
        self.levelOrderHelp(root, result, 0)
        return result

    def levelOrderHelp(self, root, result, depth) -> None:
        if root:
            if depth > len(result) - 1:
                result.append([])

            result[depth].append(root.val)
            self.levelOrderHelp(root.left, result, depth + 1)
            self.levelOrderHelp(root.right, result, depth + 1)

    def levelOrder_2(self, root: TreeNode) -> list[list[int]]:
        if not root: return []
        result = []
        queue = collections.deque([root])

        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level)

        return result


    def zigzagLevelOrder(sefl, root: TreeNode) -> list[list[int]]:
        """ left to right, then right to left for the next level and alternate between """
        if not root: return []
        queue = collections.deque([root])
        result = []
        even_level = True

        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if even_level:
                result.append(level)
            else:
                result.append(level[::-1])
            even_level = not even_level

        return result

    def buildTree(self, preorder: list[int], inorder: list[int]):
        """
        construct the binary tree with given preorder and inorder node value
        NOTE:
        when pop the preorder list in the left branch, when return, it affects the
        preorder list passed to the right branch.
        """
        if inorder:
            idx = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[idx])
            root.left = self.buildTree(preorder, inorder[0:idx])
            root.right = self.buildTree(preorder, inorder[idx+1:])
            return root

    def levelOrderConnect_1(self, root) -> TreeNode:
        """ set each node.next to the node on its right on the same level or None"""
        if not root:
            return root
        if root.left:
            root.left.next = root.right
        if root.right and root.next:
            root.right.next = root.next.left
        self.levelOrderConnect_1(root.left)
        self.levelOrderConnect_1(root.right)
        return root

    def levelOrderConnect_2(self, root) -> TreeNode:
        """ set each node.next to the node on its right on the same level or None"""
        if not root: return None
        queue = collections.deque([root])

        while queue:
            level = []
            for i in range(len(queue)):
                node = queue.popleft()
                if level:
                    level[i-1].next = node
                level.append(node)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return root


    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """
        Given a binary tree: no need left smaller than root, right bigger than root
        The lowest common ancestor is defined between two nodes p and q as the
        lowest node in T that has both p and q as descendants.
        (where we allow a node to be a descendant of itself)
        """
        stack, p_trace, q_trace = [], [], []
        if root.val == p.val or root.val == q.val:
            return root

        while True:
            if root.left:
                stack.append(root)
                root.left, root = None, root.left
            elif root.right:
                stack.append(root)
                root.right, root = None, root.right
            else:
                if root == p:
                    p_trace = stack[:]
                    p_trace.append(root)
                elif root == q:
                    q_trace = stack[:]
                    q_trace.append(root)
                elif p_trace and q_trace:
                    break
                root = stack.pop()

        idx, minLen = 0, min(len(p_trace), len(q_trace))
        while idx < minLen and p_trace[idx] is q_trace[idx]:
            result = p_trace[idx]
            idx += 1
        return result


def main():
    n8 = TreeNode(8)
    n9 = TreeNode(9)
    n10 = TreeNode(10)
    n4 = TreeNode(4)
    n5 = TreeNode(5, n8)
    n6 = TreeNode(6, n9)
    n7 = TreeNode(7, n10)
    n2 = TreeNode(2, n4, n5)
    n3 = TreeNode(3, n6, n7)
    n1 = TreeNode(1, n2, n3)

    o1 = Solution()
    print(o1.inorder(n1))
    print(o1.levelOrder_1(n1))
    print(o1.levelOrder_2(n1))
    print(o1.zigzagLevelOrder(n1))
    print(o1.inorder(o1.buildTree([1,2,4,5,3,6,7], [4,2,5,1,6,3,7])))
    root1 = o1.levelOrderConnect_1(n1)
    print(root1.next)
    print(root1.left.next.val)
    print(root1.left.left.next.val)

    root2 = o1.levelOrderConnect_2(n1)
    print(root2.next)
    print(root2.left.next.val)
    print(root2.left.right.next.val)

main()
