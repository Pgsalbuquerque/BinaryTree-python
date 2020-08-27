class Node:

    def __init__(self,key,value):
        self.value = value
        self.key = key
        self.left = None
        self.right = None
        self.father = None

    def __lt__(self,node2):
        if type(self) != type(node2):
            raise TypeError('Two different objects')
        if type(self.value) != type(node2.value):
            raise 'the types of values ​​are different'
        if self.value < node2.value:
            return True
        return False
    
    def __le__(self,node2):
        if type(self) != type(node2):
            raise TypeError('Two different objects')
        if type(self.value) != type(node2.value):
            raise 'the types of values ​​are different'
        if self.value <= node2.value:
            return True
        return False

    def __gt__(self,node2):
        if type(self) != type(node2):
            raise TypeError('Two different objects')
        if type(self.value) != type(node2.value):
            raise 'the types of values ​​are different'
        if self.value > node2.value:
            return True
        return False

    def __ge__(self,node2):
        if type(self) != type(node2):
            raise TypeError('Two different objects')
        if type(self.value) != type(node2.value):
            raise 'the types of values ​​are different'
        if self.value >= node2.value:
            return True
        return False

    '''def __eq__(self,node2):
        if type(self) != type(node2):
            return False
        if type(self.value) != type(node2.value):
            return False
        if self.value == node2.value:
            return True
        return False'''

    def __ne__(self,node2):
        if type(self) != type(node2):
            raise TypeError('Two different objects')
        if type(self.value) != type(node2.value):
            raise 'the types of values ​​are different'
        if self.value != node2.value:
            return True
        return False

class BinaryTree:

    def __init__(self,key,value=None):
        self.root = None
        if key:
            self.root = Node(key,value)

    def __bool__(self):
        if self.root == None:
            return False
        return True

    def append(self,key,value):
        if not self.root:
            self.root = Node(key,value)
        else:
            pointer = self.root
            while True:
                if pointer.key > key:
                    if pointer.left == None:
                        pointer.left = Node(key,value)
                        pointer.left.father = pointer
                        return
                    else:
                        pointer = pointer.left
                elif pointer.key < key:
                    if pointer.right == None:
                        pointer.right = Node(key,value)
                        pointer.right.father = pointer
                        return
                    else:
                        pointer = pointer.right

    def printorder(self,pointer):  
        string = ''
        if pointer.left:
            string += self.printorder(pointer.left)
        if pointer:
            string += str(pointer.key) + ','
        if pointer.right:
            string += self.printorder(pointer.right)
        return string

    def printPreOrder(self,pointer):  
        string = ''
        if pointer:
            string += str(pointer.key) + ','
        if pointer.left:
            string += self.printPreOrder(pointer.left)
        if pointer.right:
            string += self.printPreOrder(pointer.right)
        return string

    def __str__(self):
        pointer = self.root
        if pointer:
            string = self.printorder(pointer)
            return string[0:len(string)-1]
        return 'Árvore vazia'

    def __repr__(self):
        pointer = self.root
        string = self.printPreOrder(pointer)
        lista = []

        stringFlag = ''
        for x in string:
            if x != ',':
                stringFlag += x
            else:
                lista.append(stringFlag)
                stringFlag = ''

        return lista

    def __getitem__(self,key):
        pointer = self.root
        while pointer:
            if pointer.key != key:
                if pointer.key > key:
                    pointer = pointer.left
                elif pointer.key < key:
                    pointer = pointer.right
            else:
                return pointer.value
        raise KeyError('dont have this key in the  Binary Tree')
        
    def _getNode_(self,key):
        pointer = self.root
        while pointer:
            if pointer.key != key:
                if pointer.key > key:
                    pointer = pointer.left
                elif pointer.key < key:
                    pointer = pointer.right
            else:
                return pointer
        raise KeyError('dont have this key in the  Binary Tree')
    
    def __setitem__(self,key,value):
        pointer = self.root
        while pointer:
            if pointer.key != key:
                if pointer.key > key:
                    pointer = pointer.left
                elif pointer.key < key:
                    pointer = pointer.right
            else:
                pointer.value = value
                return
        raise KeyError('dont have this key in the  Binary Tree')
    
    def __contains__(self,key):
        pointer = self.root
        while pointer:
            if pointer.key != key:
                if pointer.key > key:
                    pointer = pointer.left
                elif pointer.key < key:
                    pointer = pointer.right
            else:
                return True
        return False

    def threeMinimun(self,x):
        while x.left:
            x = x.left
        return x

    def __sucessor__(self,x):
        if x.right:
            return self.threeMinimun(self._getNode_(x.right.key))
        y = x.father
        while y and x == y.right:
            x = y
            y = y.father
        return y

    def threeMaximun(self,x):
        while x.right:
            x = x.right
        return x

    def __antecessor__(self,x):
        if x.left:
            return self.threeMaximun(self._getNode_(x.left.key))
        y = x.father
        while y and x == y.left:
            x = y
            y = y.father
        return y
    
    def __delitem__(self,key):
        pointer = self._getNode_(key)
        if pointer == self.root:
            if pointer.left == None and pointer.right == None:
                self.root = None
                return
            pointer2 = self.__sucessor__(pointer)
            if pointer2.right:
                pointer3 = pointer2.right
                pointer2.father.left = pointer3
                pointer3.father = pointer2.father
            else:
                pointer2.father.left = None
            pointer2.father = None
            pointer2.left = pointer.left
            pointer2.right = pointer.right
            self.root = pointer2
            if self.root.left:
                self.root.left.father = pointer2
            self.root.right.father = pointer2
            pointer.father = None
            pointer.left = None
            pointer.right = None
        elif pointer.left is None:
            if pointer.right:
                pointer2 = pointer.father
                if pointer2.left == pointer:
                    pointer2.left = pointer.right
                    pointer.right.father = pointer2
                else:
                    pointer2.right = pointer.right
                    pointer.right.father = pointer2
            else:
                pointer2 = pointer.father
                if pointer2.right == pointer:
                    pointer2.right = None
                    pointer.father = None
                else:
                    pointer2.left = None
                    pointer.father = None
        elif pointer.right is None:
            if pointer.left:
                pointer2 = pointer.father
                if pointer2.left == pointer:
                    pointer2.left = pointer.left
                    pointer.left.father = pointer2
                else:
                    pointer2.right = pointer.left
                    pointer.left.father = pointer2
            else:
                pointer2 = pointer.father
                if pointer2.right == pointer:
                    pointer2.right = None
                    pointer.father = None  

        elif pointer.right and pointer.left:
            pointer2 = pointer.father
            pointer3 = self.__sucessor__(self._getNode_(key))
            if pointer3.right:
                pointer4 = pointer3.right
                pointer3.father.left = pointer4
                pointer4.father = pointer3.father
            else:
                pointer3.father.left = None

            if pointer2.left == pointer:
                pointer2.left = pointer3
                pointer3.father = pointer2
                pointer3.left = pointer.left
                pointer3.left.father = pointer3
                pointer3.right = pointer.right
                pointer3.right.father = pointer3
            
            elif pointer2.right == pointer:
                pointer2.right = pointer3
                pointer3.father = pointer2
                pointer3.left = pointer.left
                if pointer.left:
                    pointer3.left.father = pointer3
                pointer3.right = pointer.right
                pointer3.right.father = pointer3
        return 

    def reiniciar(self):
        pointer = self.root
        return self._reiniciar(pointer)

    def _reiniciar(self,pointer):
        if pointer:
            if pointer.left:
                 self._reiniciar(pointer.left)
            if pointer.right:
                self._reiniciar(pointer.right)
            x = pointer.key
            del self[pointer.key]
            return x

    def __keys(self,no,chaves=[]):
        if no is not None: 
            chaves.append(no.key)
            chaves = self.__keys(no.left, chaves)
            chaves = self.__keys(no.right, chaves)
        return chaves
    
    def __iter__(self):
        return iter(self.__keys(self.root,[]))
    

