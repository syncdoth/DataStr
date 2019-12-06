# DataStr
 Custom made Python Data Structures

Data Structures included right now:

* Stack
* Queue
* BST (Binary Search Tree)

To be added:

* AVL
* Hash
* Trie


*Since the whole module is written in Python3, all the data structures support generic programming natively.*

## BST Implementation
The BST implementation inspired from HKUST 2012H Course's C++ approach, in which the design of the structure is as follows:

contains two class, BST and BSTNode.

* BST {

  * BSTNode type root object

}

* BSTNode {

  * data object
  * BST type left Tree
  * BST type right Tree

}

Such definition allows for the left subtree and right subtree are in fact trees, BST objects, not tree nodes, BSTNode objects. This simplifies the code, allowing for subtrees to use the methods of the tree (not that of a node), and thereby improves readability.
