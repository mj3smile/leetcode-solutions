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
        if root:
            queue.append(root)
        
        result = ""
        while len(queue) > 0:
            for _ in range(len(queue)):
                node = queue.popleft()
                comma = ","
                if result == "":
                    comma = ""

                if node:
                    result = result + comma + str(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
                else:
                    result = result + comma + "null"
                    # queue.append(None)
                    # queue.append(None)
                # print("result:", result)

        # print("result:", result)
        return result

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        
        data_arr = data.split(",")
        print("data_arr:", data_arr)
        queue = deque()
        root = None
        if data_arr:
            if data_arr[0] == "null" or data_arr[0] == "": return
            root = TreeNode(int(data_arr[0])) 
            queue.append(root)
        
        i = 1
        while i < len(data_arr):
            # print(data_arr[i], data_arr[i + 1])
            root_node = queue.popleft()
            if not root_node:
                # print("root node: null")
                continue
            # print("root node:", root_node.val)
            left = data_arr[i]
            if i < len(data_arr) - 1: right = data_arr[i + 1]

            left_node = None
            if left != "null":
                left_node = TreeNode(int(left))
            
            right_node = None
            if right != "" and right != "null":
                right_node = TreeNode(int(right))
            
            root_node.left = left_node
            root_node.right = right_node
            queue.append(left_node)
            queue.append(right_node)
            i += 2
        
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))