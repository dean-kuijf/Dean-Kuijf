#Árvore Binária de Procura (BST)(feito em aula):
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, root, key):
        if key < root.val:
            if root.left is None:
                root.left = Node(key)
            else:
                self._insert(root.left, key)
        else:
            if root.right is None:
                root.right = Node(key)
            else:
                self._insert(root.right, key)

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, root, key):
        if root is None or root.val == key:
            return root
        if key < root.val:
            return self._search(root.left, key)
        return self._search(root.right, key)

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, root, key):
        if root is None:
            return root
        if key < root.val:
            root.left = self._delete(root.left, key)
        elif key > root.val:
            root.right = self._delete(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            temp = self._min_value_node(root.right)
            root.val = temp.val
            root.right = self._delete(root.right, temp.val)
        return root

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current


#Árvore AVL(feito em aula(foi só copy paste)): 
class AVLNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
        self.height = 1

class AVL:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, root, key):
        if root is None:
            return AVLNode(key)
        if key < root.val:
            root.left = self._insert(root.left, key)
        else:
            root.right = self._insert(root.right, key)

        root.height = 1 + max(self._get_height(root.left), self._get_height(root.right))

        balance = self._get_balance(root)

        if balance > 1 and key < root.left.val:
            return self._right_rotate(root)
        if balance < -1 and key > root.right.val:
            return self._left_rotate(root)
        if balance > 1 and key > root.left.val:
            root.left = self._left_rotate(root.left)
            return self._right_rotate(root)
        if balance < -1 and key < root.right.val:
            root.right = self._right_rotate(root.right)
            return self._left_rotate(root)

        return root

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, root, key):
        if root is None or root.val == key:
            return root
        if key < root.val:
            return self._search(root.left, key)
        return self._search(root.right, key)

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, root, key):
        if not root:
            return root
        if key < root.val:
            root.left = self._delete(root.left, key)
        elif key > root.val:
            root.right = self._delete(root.right, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            temp = self._min_value_node(root.right)
            root.val = temp.val
            root.right = self._delete(root.right, temp.val)

        if root is None:
            return root

        root.height = 1 + max(self._get_height(root.left), self._get_height(root.right))

        balance = self._get_balance(root)

        if balance > 1 and self._get_balance(root.left) >= 0:
            return self._right_rotate(root)
        if balance < -1 and self._get_balance(root.right) <= 0:
            return self._left_rotate(root)
        if balance > 1 and self._get_balance(root.left) < 0:
            root.left = self._left_rotate(root.left)
            return self._right_rotate(root)
        if balance < -1 and self._get_balance(root.right) > 0:
            root.right = self._right_rotate(root.right)
            return self._left_rotate(root)

        return root

    def _left_rotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
        return y

    def _right_rotate(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
        return y

    def _get_height(self, root):
        if not root:
            return 0
        return root.height

    def _get_balance(self, root):
        if not root:
            return 0
        return self._get_height(root.left) - self._get_height(root.right)

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current


#Geração de Dados de Teste
#Para avaliar as árvores com diferentes tamanhos, vamos criar conjuntos de dados ordenados e aleatórios
import random

def generate_ordered_data(size):
    return list(range(size))

def generate_random_data(size):
    data = list(range(size))
    random.shuffle(data)
    return data

#Avaliação de Desempenho
#Vamos usar a biblioteca time para medir o tempo das operações.

import time

def measure_insertion(tree, data):
    start_time = time.time()
    for key in data:
        tree.insert(key)
    end_time = time.time()
    return end_time - start_time

def measure_search(tree, data):
    start_time = time.time()
    for key in data:
        tree.search(key)
    end_time = time.time()
    return end_time - start_time

def measure_deletion(tree, data):
    start_time = time.time()
    for key in data:
        tree.delete(key)
    end_time = time.time()
    return end_time - start_time

#Comparação de Desempenho
#Para comparar as BST e AVL, vamos medir o tempo das operações para diferentes tamanhos de dados e gerar gráficos com os resultados.

import matplotlib.pyplot as plt

sizes = [100, 1000, 10000]
results = {
    "BST": {"insert": [], "search": [], "delete": []},
    "AVL": {"insert": [], "search": [], "delete": []}
}

for size in sizes:
    ordered_data = generate_ordered_data(size)
    random_data = generate_random_data(size)
    
    bst = BST()
    avl = AVL()
    

    results["BST"]["insert"].append(measure_insertion(bst, random_data))
    results["BST"]["search"].append(measure_search(bst, random_data))
    results["BST"]["delete"].append(measure_deletion(bst, random_data))

    results["AVL"]["insert"].append(measure_insertion(avl, random_data))
    results["AVL"]["search"].append(measure_search(avl, random_data))
    results["AVL"]["delete"].append(measure_deletion(avl, random_data))
# Plot dos resultados
plt.figure(figsize=(12, 6))
plt.subplot(1, 3, 1)
plt.plot(sizes, results["BST"]["insert"], label='BST Insert')
plt.plot(sizes, results["AVL"]["insert"], label='AVL Insert')
plt.xlabel('Number of Elements')
plt.ylabel('Time (seconds)')
plt.title('Insertion Time')
plt.legend()

plt.subplot(1, 3, 2)
plt.plot(sizes, results["BST"]["search"], label='BST Search')
plt.plot(sizes, results["AVL"]["search"], label='AVL Search')
plt.xlabel('Number of Elements')
plt.ylabel('Time (seconds)')
plt.title('Search Time')
plt.legend()

plt.subplot(1, 3, 3)
plt.plot(sizes, results["BST"]["delete"], label='BST Delete')
plt.plot(sizes, results["AVL"]["delete"], label='AVL Delete')
plt.xlabel('Number of Elements')
plt.ylabel('Time (seconds)')
plt.title('Deletion Time')
plt.legend()

plt.tight_layout()
plt.show()

#APENAS CONSEGUI FAZER OS GRAFICOS PARA OS ALEATORIOS OS ORDENADOS NÃO SEI O QUE FIZ MAL NA RECURSIVIDADE :()





















