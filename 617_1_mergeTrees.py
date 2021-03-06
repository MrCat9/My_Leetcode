# -*- coding: utf-8 -*-
# 广度优先遍历


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

        node_list = [(root1, root2)]
        while node_list:
            node1, node2 = node_list.pop(0)
            v1 = node1.val
            v2 = node2.val  # if node2.val else 0
            node1.val = v1 + v2
            # if node1.val == 0:
            #     node1.val = None

            if node2.left:
                if not node1.left:
                    node1.left = TreeNode()
                node_list.append((node1.left, node2.left))
            if node2.right:
                if not node1.right:
                    node1.right = TreeNode()
                node_list.append((node1.right, node2.right))

        return root1


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
