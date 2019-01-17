from tree import *

def template_preorder_traversal(preorder):
    root = deserialize('[2,2,3,null,null,4,null,null,5]')
    assert preorder(root) == [2,2,3,4,5]
    root = deserialize('[2,1,3,0,7,9,1,2,null,1,0,null,null,8,8,null,null,null,null,7]') 
    assert preorder(root) == [2,1,0,2,7,1,0,7,3,9,1,8,8]

def test_preorder_traversal_recursive():
    template_preorder_traversal(preorder_traversal_recursive)

def test_preorder_traversal_iterative():
    template_preorder_traversal(preorder_traversal_iterative)

def test_preorder_traversal_iterative_ptr():
    template_preorder_traversal(preorder_traversal_iterative_ptr)

def template_postorder_traversal(postorder):
    root = deserialize('[2,2,3,null,null,4,null,null,5]')
    assert postorder(root) == [2,5,4,3,2]
    root = deserialize('[2,1,3,0,7,9,1,2,null,1,0,null,null,8,8,null,null,null,null,7]') 
    assert postorder(root) == [2,0,1,7,0,7,1,9,8,8,1,3,2]

def test_postorder_traversal_recursive():
    template_postorder_traversal(postorder_traversal_recursive)

def test_postorder_traversal_iterative():
    template_postorder_traversal(postorder_traversal_iterative)

def test_postorder_traversal_iterative_pre():
    template_postorder_traversal(postorder_traversal_iterative_pre)

def test_postorder_traversal_iterative_ptr():
    template_postorder_traversal(postorder_traversal_iterative_ptr)

def template_inorder_traversal(inorder):
    root = deserialize('[2,2,3,null,null,4,null,null,5]')
    assert inorder(root) == [2,2,4,5,3]
    root = deserialize('[2,1,3,0,7,9,1,2,null,1,0,null,null,8,8,null,null,null,null,7]') 
    assert inorder(root) == [2,0,1,1,7,7,0,2,9,3,8,1,8]

def test_inorder_traversal_recursive():
    template_inorder_traversal(inorder_traversal_recursive)

def test_inorder_traversal_iterative_ptr():
    template_inorder_traversal(inorder_traversal_iterative_ptr)

def test_level_traversal():
    root = deserialize('[2,2,3,null,null,4,null,null,5]')
    assert level_traversal(root) == [2,2,3,4,5]
    root = deserialize('[2,1,3,0,7,9,1,2,null,1,0,null,null,8,8,null,null,null,null,7]') 
    assert level_traversal(root) == [2,1,3,0,7,9,1,2,1,0,8,8,7]

