from AVLtree import AVLtree
from bst import BST
from matplotlib import pyplot as plt
import random
import gc
import time


def create(tree, test_list):
    gc_old = gc.isenabled()
    gc.disable()
    start = time.process_time()
    tree(test_list)
    stop = time.process_time()
    time_taken = stop - start
    if gc_old:
        gc.enable()
    return time_taken


def create_test():
    treesnames = {
        BST: "Binary Search Tree", AVLtree: "AVL Tree"
    }
    test_list = []
    for n in range(10000):
        test_list.append(random.randint(1, 30000))
    for tree in treesnames.keys():
        elemrecords = []
        timerecords = []
        currlim = 0
        section = int(len(test_list) / 10)
        currlim += section
        while currlim <= len(test_list):
            time_taken = create(tree, test_list[1:currlim])
            elemrecords.append(currlim)
            timerecords.append(time_taken)
            currlim += section
        plt.plot(elemrecords, timerecords, label=treesnames.get(tree))
    plt.ylabel('Czas wykonania (sekundy)')
    plt.xlabel('Ilość liczb')
    plt.title('Czas tworzenia drzew dla 10000 liczb.')
    plt.legend()
    plt.savefig(fname='create_trees.png')
    plt.show()


def search(tree, test_list):
    gc_old = gc.isenabled()
    gc.disable()
    start = time.process_time()
    for n in range(len(test_list)):
        tree.findNode(test_list[n])
    stop = time.process_time()
    time_taken = stop - start
    if gc_old:
        gc.enable()
    return time_taken


def search_test():
    treesnames = {
        BST: "Binary Search Tree", AVLtree: "AVL Tree"
    }
    test_list = []
    for n in range(10000):
        test_list.append(random.randint(1, 30000))
    for tree in treesnames.keys():
        tree_test = tree(test_list)
        elemrecords = []
        timerecords = []
        currlim = 0
        section = int(len(test_list) / 10)
        currlim += section
        while currlim <= len(test_list):
            time_taken = search(tree_test, test_list[1:currlim])
            elemrecords.append(currlim)
            timerecords.append(time_taken)
            currlim += section
        plt.plot(elemrecords, timerecords, label=treesnames.get(tree))
    plt.ylabel('Czas wykonania (sekundy)')
    plt.xlabel('Ilość liczb')
    plt.title('Czas szukania w drzewach dla 10000 liczb.')
    plt.legend()
    plt.savefig(fname='search_trees.png')
    plt.show()


def delete(bst, test_list):
    gc_old = gc.isenabled()
    gc.disable()
    start = time.process_time()
    for n in range(len(test_list)):
        bst.deleteNode(test_list[n])
    stop = time.process_time()
    time_taken = stop - start
    if gc_old:
        gc.enable()
    return time_taken


def delete_test():
    test_list = []
    for n in range(10000):
        test_list.append(random.randint(1, 30000))
    elemrecords = []
    timerecords = []
    currlim = 0
    section = int(len(test_list) / 10)
    currlim += section
    while currlim <= len(test_list):
        bst = BST(test_list)
        time_taken = delete(bst, test_list[1:currlim])
        elemrecords.append(currlim)
        timerecords.append(time_taken)
        currlim += section
    plt.plot(elemrecords, timerecords, label="Binary Search Tree")
    plt.ylabel('Czas wykonania (sekundy)')
    plt.xlabel('Ilość liczb')
    plt.title('Czas usuwania w BST dla 10000 liczb.')
    plt.legend()
    plt.savefig(fname='bst_delete.png')
    plt.show()


def main():
    if __name__ == "__main__":
        create_test()
        search_test()
        delete_test()


main()
