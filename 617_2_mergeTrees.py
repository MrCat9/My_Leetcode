# -*- coding: utf-8 -*-
# 深度优先遍历


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        if not root2:
            return root1
        if not root1:
            return root2

        new_node = TreeNode(
            val=root1.val + root2.val,
            left=self.mergeTrees(root1.left, root2.left),
            right=self.mergeTrees(root1.right, root2.right),
        )

        return new_node


if __name__ == '__main__':

    def gen_tree(val_list: list):
        vl_len = len(val_list)
        root_node = TreeNode(
            val=val_list[0]
        )
        node = root_node
        layer_node = [node]
        new_layer_node = []
        i = 1

        while True:
            for node in layer_node:
                v = val_list[i] if val_list[i] else 0
                new_node = TreeNode(val=v)
                i += 1
                new_layer_node.append(new_node)
                node.left = new_node
                if i >= vl_len:
                    break

                v = val_list[i] if val_list[i] else 0
                new_node = TreeNode(val=v)
                i += 1
                new_layer_node.append(new_node)
                node.right = new_node
                if i >= vl_len:
                    break
            if i >= vl_len:
                break
            layer_node = new_layer_node
            new_layer_node = []

        return root_node


    test_root1 = gen_tree(val_list=[1, 3, 2, 5])
    test_root2 = gen_tree(val_list=[2, 1, 3, None, 4, None, 7])
    Solution().mergeTrees(test_root1, test_root2)
