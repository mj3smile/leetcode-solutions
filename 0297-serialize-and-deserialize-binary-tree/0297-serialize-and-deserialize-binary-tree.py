# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        queue = deque()
        queue.append(root)
        
        result = ""
        while queue:
            for _ in range(len(queue)):
                comma = ","
                if result == "":
                    comma = ""

                node = queue.popleft()
                if not node:
                    result += comma + "null"
                    continue
                
                result += comma + str(node.val)
                queue.append(node.left)
                queue.append(node.right)

        return result
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """

        root = None
        serialized_nodes = data.split(",")

        if serialized_nodes:
            root = self.deserialize_node(serialized_nodes[0])
        
        roots = deque()
        roots.append(root)
        i = 1
        while roots and i < len(serialized_nodes) - 1:
            current_root = roots.popleft()
            if not current_root:
                continue

            left = self.deserialize_node(serialized_nodes[i])
            right = self.deserialize_node(serialized_nodes[i + 1])
            current_root.left = left
            current_root.right = right
            roots.append(left)
            roots.append(right)
            i += 2
        
        return root

    
    def deserialize_node(self, serialized_node):
        if serialized_node == "null":
            return None
        
        value = 0
        try:
            value = int(serialized_node)
        except:
            return None
        
        return TreeNode(value)





# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))