class TreeNode:
    # BST에서 삽입되는 노드는 항상 단말 노드가 된다.
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def insert(root, key):
    if root == None:
        return TreeNode(key)
    
    if key < root.key:
        # 재귀호출. root.left가 None이면 들어갈 노드를 만들어준다.
        root.left = insert(root.left, key)
    
    elif key > root.key:
        # tree 연산은 항상 symmetric
        root.right = insert(root.right, key)
        
    return root
    # else를 안쓰는 이유 : 같을 경우 삽입을 생략하기 위해

def inOrder(root):
    if root:
        inOrder(root.left)
        print('%2d ' % root.key, end = ' ')
        inOrder(root.right)

def display(root, msg):
    print(msg, end = " ")
    inOrder(root)
    print()
    
def minKeyNode(root):
    while root != None and root.left != None:
        root = root.left

    return root

# root는 트리가 날아온다고 생각
def delete(root, key):
    if root == None:
        return None
    
    if key < root.key:
        # 재귀호출. root.left가 None이면 들어갈 노드를 만들어준다.
        root.left = delete(root.left, key)
    
    elif key > root.key:
        # tree 연산은 항상 symmetric
        root.right = delete(root.right, key)
    
    else:
        # 왼쪽 자식 노드가 없다
        if root.left == None:
            return root.right
        
        elif root.right == None:
            return root.left
        
        # 다른 적절한 어떤 값으로 덮어쓴다 어떤 값 : 전위 혹은 후위 계승자
        # inOrder 순회하면 키가 오름차순으로 정렬됨 전위계승자 : 삭제할 키의 바로 앞 후위 : 바로 뒤
        # 왼쪽 서브 트리의 가장 키의 크기가 큰 노드 : 왼쪽 서브트리의 맨 오른쪽
        # 오른쪽 서브 트리의 가장 키의 크기가 작은 노드 : 오른쪽 서브트리의 맨 왼쪽
        # 계승자는 단말노드 : case 1에 걸림 -> 간단하게 삭제 가능
        else:
            succ = minKeyNode(root.right)
            root.key = succ.key
            root.right = delete(root.right, succ.key)
        
    return root

if __name__ == "__main__":
    root = None
    data = [35, 18, 7, 26, 3, 22, 30, 12, 26, 68, 99]
    
    for key in data:
        root = insert(root, key)
        # root의 키가 중간값에서 멀어지면 트리가 편향적이다.
        display(root, "[Insert %2d] :" %key)
    print()
    
    # root = delete(root, 30)
    # display(root, "[Delete 30] :")
    # root = delete(root, 26)
    # display(root, "[Delete 26] :")
    
    root = delete(root, 35)
    display(root, "[Delete 30] :")