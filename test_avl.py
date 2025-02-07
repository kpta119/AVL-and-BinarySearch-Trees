from AVLtree import AVLtree


def test_find_node():
    tree = AVLtree([10, 20, 30, 27, 28])
    assert tree.findNode(10).value == 10
    assert tree.findNode(20).value == 20
    assert tree.findNode(30).value == 30
    assert tree.findNode(27).value == 27
    assert tree.findNode(28).value == 28


def test_create_tree():
    tree = AVLtree([10, 20, 30, 27, 28])
    assert tree.root.value == 20
    assert tree.findNode(10)
    assert tree.findNode(30)
    assert tree.findNode(27)
    assert tree.findNode(28)


def test_insert_key():
    tree = AVLtree([1, 2, 3, 8, 6, 4])
    assert not tree.findNode(10)
    tree.insert(tree.root, 10)
    assert tree.findNode(10)


def test_insert_the_same_key():
    tree = AVLtree([1, 2, 3, 8, 6, 4])
    tree.insert(tree.root, 1)
    assert tree.findNode(1)

    