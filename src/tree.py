from treeutil import *
import collections

def preorder_traversal_recursive(root):
    def _dfs(node, res):
        if not node: return
        res.append(node.val)
        _dfs(node.left, res)
        _dfs(node.right, res)
    res = []
    _dfs(root, res)
    return res

def preorder_traversal_iterative(root):
    res = []
    st = collections.deque([root])
    while st:
        node = st.pop()
        res.append(node.val)
        if node.right: st.append(node.right)
        if node.left: st.append(node.left) 
    return res

def preorder_traversal_iterative_ptr(root):
    res = []
    st = collections.deque()
    p = root
    while st or p:
        if p:
            st.append(p)
            res.append(p.val)
            p = p.left
        else:
            t = st.pop()
            p = t.right
    return res

def postorder_traversal_recursive(root):
    def _dfs(node, res):
        if not node: return
        _dfs(node.left, res)
        _dfs(node.right,res)
        res.append(node.val)
    res = []
    _dfs(root, res)
    return res

# reverse output order of preorder (w/ left right swapped)
def postorder_traversal_iterative(root):
    res = []
    st = collections.deque([root])
    while st:
        node = st.pop()
        res.append(node.val)
        if node.left: st.append(node.left)
        if node.right: st.append(node.right)
    return res[::-1]

def postorder_traversal_iterative_ptr(root):
    res = []
    st = collections.deque()
    p = root
    while st or p:
        if p:
            st.append(p)
            res.append(p.val)
            p = p.right
        else:
            t = st.pop()
            p = t.left
    return res[::-1]

# hard and direct method
def postorder_traversal_iterative_pre(root):
    res = []
    st = collections.deque([root])
    pre = TreeNode(None)  # cannot be None, otherwise confusing with leaf left or right. or use root instead
    while st:
        node = st[-1]  # unlike preorder: need to maintain st without popping before completion
        if (not node.left and not node.right) or (node.left==pre or node.right==pre):  # either a leaf or traceback
            res.append(node.val)
            pre = st.pop()
        else:
            if node.right: st.append(node.right)
            if node.left: st.append(node.left)
    return res

def inorder_traversal_recursive(root):
    def _dfs(node, res):
        if not node: return
        if node.left: _dfs(node.left, res)
        res.append(node.val)
        if node.right: _dfs(node.right, res)
    res = []
    _dfs(root, res)
    return res

def inorder_traversal_iterative_ptr(root):
    res = []
    if not root: return res
    st = collections.deque()
    p = root
    while st or p:
        if p:
            st.append(p)
            p = p.left
        else:
            t = st.pop()
            res.append(t.val)
            p = t.right
    return res
            
def level_traversal(root):
    res = []
    q = collections.deque([root])
    while q:
        n = len(q)
        for _ in range(n):
            node = q.popleft()
            res.append(node.val)
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
    return res

