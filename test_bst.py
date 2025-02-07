from bst import BST


def test_bst_create():
    bst = BST([1, 2, 3, 4, 5, 6])
    assert bst.findNode(1)
    assert bst.findNode(2)
    assert bst.findNode(3)
    assert bst.findNode(4)
    assert bst.findNode(5)
    assert bst.findNode(6)


def test_bst_insert():
    bst = BST([0, 4, 1, 8, 10, 3])
    assert not bst.findNode(12)
    bst.insert(12)
    assert bst.findNode(12)


def test_bst_delete():
    bst = BST([1, 2, 3, 4, 5, 6])
    assert bst.findNode(2)
    bst.deleteNode(2)
    assert not bst.findNode(2)
    assert bst.findNode(6)
    bst.deleteNode(6)
    assert not bst.findNode(6)
    assert bst.findNode(1)
    bst.deleteNode(1)
    assert not bst.findNode(1)
