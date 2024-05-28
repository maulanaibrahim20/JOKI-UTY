{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "None\n"
     ]
    }
   ],
   "source": [
    "class Node:\n",
    "    def __init__(self, value):\n",
    "        self.value = value\n",
    "        self.left = None\n",
    "        self.right = None\n",
    "\n",
    "class BinarySearchTree:\n",
    "    def __init__(self):\n",
    "        self.root = None\n",
    "\n",
    "my_tree = BinarySearchTree()\n",
    "print(my_tree.root)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Root: 2\n",
      "Root->Left: 1\n",
      "Root->Right: 3\n"
     ]
    }
   ],
   "source": [
    "class Node:\n",
    "    def __init__(self, value):\n",
    "        self.value = value\n",
    "        self.left = None\n",
    "        self.right = None\n",
    "class BinarySearchTree:\n",
    "    def __init__(self):\n",
    "        self.root = None\n",
    "    \n",
    "    def insert(self, value):\n",
    "        new_node = Node(value)\n",
    "        if self.root is None:\n",
    "            self.root = new_node\n",
    "            return True\n",
    "        temp = self.root\n",
    "        while (True):\n",
    "            if new_node.value == temp.value:\n",
    "                return False\n",
    "            if new_node.value < temp.value:\n",
    "                if temp.left is None:\n",
    "                    temp.left = new_node\n",
    "                    return True\n",
    "                temp = temp.left\n",
    "            else:\n",
    "                if temp.right is None:\n",
    "                    temp.right = new_node\n",
    "                    return True\n",
    "                temp = temp.right\n",
    "\n",
    "my_tree = BinarySearchTree()\n",
    "my_tree.insert(2)\n",
    "my_tree.insert(1)\n",
    "my_tree.insert(3)\n",
    "\n",
    "print('Root:', my_tree.root.value)\n",
    "print('Root->Left:', my_tree.root.left.value)\n",
    "print('Root->Right:', my_tree.root.right.value)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "BST Contains 27:\n",
      "True\n",
      "\n",
      "BST Contains 17:\n",
      "False\n"
     ]
    }
   ],
   "source": [
    "class Node:\n",
    "    def __init__(self, value):\n",
    "        self.value = value\n",
    "        self.left = None\n",
    "        self.right = None\n",
    "\n",
    "class BinarySearchTree:\n",
    "    def __init__(self):\n",
    "        self.root = None\n",
    "\n",
    "    def insert(self, value):\n",
    "        new_node = Node(value)\n",
    "        if self.root is None:\n",
    "            self.root = new_node\n",
    "            return True\n",
    "        temp = self.root\n",
    "        while True:\n",
    "            if new_node.value == temp.value:\n",
    "                return False\n",
    "            if new_node.value < temp.value:\n",
    "                if temp.left is None:\n",
    "                    temp.left = new_node\n",
    "                    return True\n",
    "                temp = temp.left\n",
    "            else:\n",
    "                if temp.right is None:\n",
    "                    temp.right = new_node\n",
    "                    return True\n",
    "                temp = temp.right\n",
    "\n",
    "    def contains(self, value):\n",
    "        temp = self.root\n",
    "        while temp is not None:\n",
    "            if value < temp.value:\n",
    "                temp = temp.left\n",
    "            elif value > temp.value:\n",
    "                temp = temp.right\n",
    "            else:\n",
    "                return True\n",
    "        return False\n",
    "\n",
    "my_tree = BinarySearchTree()\n",
    "my_tree.insert(47)\n",
    "my_tree.insert(21)\n",
    "my_tree.insert(76)\n",
    "my_tree.insert(18)\n",
    "my_tree.insert(27)\n",
    "my_tree.insert(52)\n",
    "my_tree.insert(82)\n",
    "\n",
    "print('BST Contains 27:')\n",
    "print(my_tree.contains(27))\n",
    "\n",
    "print('\\nBST Contains 17:')\n",
    "print(my_tree.contains(17))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Minimum value in Tree:\n",
      "18\n"
     ]
    }
   ],
   "source": [
    "class Node:\n",
    "    def __init__(self, value):\n",
    "        self.value = value\n",
    "        self.left = None\n",
    "        self.right = None\n",
    "\n",
    "class BinarySearchTree:\n",
    "    def __init__(self):\n",
    "        self.root = None\n",
    "\n",
    "    def insert(self, value):\n",
    "        new_node = Node(value)\n",
    "        if self.root is None:\n",
    "            self.root = new_node\n",
    "            return True\n",
    "        temp = self.root\n",
    "        while True:\n",
    "            if new_node.value == temp.value:\n",
    "                return False\n",
    "            if new_node.value < temp.value:\n",
    "                if temp.left is None:\n",
    "                    temp.left = new_node\n",
    "                    return True\n",
    "                temp = temp.left\n",
    "            else:\n",
    "                if temp.right is None:\n",
    "                    temp.right = new_node\n",
    "                    return True\n",
    "                temp = temp.right\n",
    "\n",
    "    def contains(self, value):\n",
    "        temp = self.root\n",
    "        while temp is not None:\n",
    "            if value < temp.value:\n",
    "                temp = temp.left\n",
    "            elif value > temp.value:\n",
    "                temp = temp.right\n",
    "            else:\n",
    "                return True\n",
    "        return False\n",
    "\n",
    "    def min_value_node(self, current_node):\n",
    "        while current_node.left is not None:\n",
    "            current_node = current_node.left\n",
    "        return current_node\n",
    "\n",
    "my_tree = BinarySearchTree()\n",
    "my_tree.insert(47)\n",
    "my_tree.insert(21)\n",
    "my_tree.insert(76)\n",
    "my_tree.insert(18)\n",
    "my_tree.insert(27)\n",
    "my_tree.insert(52)\n",
    "my_tree.insert(82)\n",
    "\n",
    "print('Minimum value in Tree:')\n",
    "print(my_tree.min_value_node(my_tree.root).value)\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
