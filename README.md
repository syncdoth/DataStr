# DataStr
 Custom made Python Data Structures

Data Structures included right now:

* Stack
* Queue
* BST (Binary Search Tree)
* Hash

To be added:

* AVL
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

## Hash Implementation
The Hash class follows such structure:

* Hash {
  * size of the table
  * the table (python list object)
  * the states list (python list object)
  * R value (used for 2nd hash function)

}

Takes the input size m and R in the constructor.


### Public functions

* Insert
  * insert the value and key to the right index
  * takes input value and key
* Search
  * search and return the item at the right index from the key
  * takes input key
* Delete
  * deletes the item at the key (lazy deletion)
  * takes input key

### Inner workings
The Hash table utilizes quadratic probing, although it takes R value which is used for second hash function for the purpose of double Hashing.

Before probing, the string key is transformed into list of integers, according to the ascii table.

Delete function uses lazy deletion: so the states list is needed. 'E' for empty, 'A' for Active, 'D' for deleted.

Each item is stored in the table as a tuple of (value, key).

Rehash function is yet to be written.
