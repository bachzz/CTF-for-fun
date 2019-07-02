class BinaryTree:
    def __init__(self, key=None):
        self.key = key
        self.left = None
        self.right = None
 
    def set_root(self, key):
        self.key = key

    def preorder(self):
        print(self.key, end=' ')
        if self.left is not None:
            self.left.preorder()
        if self.right is not None:
            self.right.preorder()
				
    def inorder(self):
        if self.left is not None:
            self.left.inorder()
        print(self.key, end=' ')
        if self.right is not None:
            self.right.inorder()
 
    def postorder(self):
        if self.left is not None:
            self.left.postorder()
        if self.right is not None:
            self.right.postorder()
        print(self.key, end=' ')
 
 
def construct_btree(postord, inord):
    if postord == [] or inord == []:
        return None
    key = postord[-1]
    node = BinaryTree(key)
    index = inord.index(key)
    node.left = construct_btree(postord[:index], inord[:index])
    node.right = construct_btree(postord[index:-1], inord[index + 1:])
    return node
 
 
postord = input('Input post-order traversal: ').split()
postord = [int(x) for x in postord]
inord = input('Input in-order traversal: ').split()
inord = [int(x) for x in inord]
 
btree = construct_btree(postord, inord)
print('Binary tree constructed.')
print('Verifying:')
print('Post-order traversal: ', end='')
btree.postorder()
print()
print('In-order traversal: ', end='')
btree.inorder()
print()
print('Pre-order traversal: ', end='')
btree.preorder()
print()
