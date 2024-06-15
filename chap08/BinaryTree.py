import queue
class TreeNode:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self):
        self.root = None
        
    def preOrder(self, node):
        if node != None:
            print('[%c]'%node.data, end =' ')
            self.preOrder(node.left)
            self.preOrder(node.right)
            
    def inOrder(self, node):
        if node != None:
            self.inOrder(node.left)
            print('[%c]'%node.data, end =' ')
            self.inOrder(node.right)
            
    def postOrder(self, node):
        if node != None:
            self.postOrder(node.left)
            self.postOrder(node.right)
            print('[%c]'%node.data, end =' ')
    
    def levelOrder(self, node):
        if node != None:
            Q = queue.Queue()
            Q.put(node)
            while not Q.empty():
                node = Q.get()
                print('[%c]'% node.data, end = ' ')
                if node.left != None:
                    Q.put(node.left)
                
                if node.right != None:
                    Q.put(node.right)
                    
    def getNodeCount(self, node):
        count = 0
        if node != None:
            count = 1 + self.getNodeCount(node.left) \
                    + self.getNodeCount(node.right)
        return count
    
    def isExternal(self, node):
        return node.left == None and node.right == None
    
    def getLeafCount(self, node):
        count = 0
        if node != None:
            if self.isExternal(node):
                return 1
            else:
                count = self.getLeafCount(node.left) \
                        + self.getLeafCount(node.right)
        return count
    
    # 이걸 꼭 손으로 해보세요
    def getHeight(self, node):
        if node == None:
            return 0
        
        return max(self.getHeight(node.left), self.getHeight(node.right)) + 1

if __name__ == "__main__":
    T = BinaryTree()
    
    # 아래부터 만드는 걸로 할게요
    
    N4 = TreeNode('D', None, None)
    N5 = TreeNode('E', None, None)
    N6 = TreeNode('F', None, None)
    N2 = TreeNode('B', N4, N5)
    N3 = TreeNode('C', N6, None)
    N1 = TreeNode('A', N2, N3)
    
    print('Pre   :', end = ' '); T.preOrder(N1); print()
    print('In    :', end = ' '); T.inOrder(N1); print()
    print('Post  :', end = ' '); T.postOrder(N1); print()
    print('Level :', end = ' '); T.levelOrder(N1); print()
    print('Num of Nodes  : %d' %T.getNodeCount(N1))
    print('Num of Leaves : %d' %T.getLeafCount(N1))