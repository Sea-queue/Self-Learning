class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: TreeNode) -> list[int]:
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


    def levelOrder(self, root: TreeNode) -> list[list[int]]:
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
    print(o1.inorderTraversal(n1))
    print(o1.levelOrder(n1))


main()
