# Name: Suhrob Hasanov 
# OSU Email: hasanovs@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: Assignment 5
# Due Date: 3/6/23
# Description: Implementation of Heap

from dynamic_array import *


class MinHeapException(Exception):
    """
    Custom exception to be used by MinHeap class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class MinHeap:

    def __init__(self, start_heap=None):
        """
        Initialize a new MinHeap
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._heap = DynamicArray()

        # populate MH with initial values (if provided)
        # before using this feature, implement add() method
        if start_heap:
            for node in start_heap:
                self.add(node)

    def __str__(self) -> str:
        """
        Return MH content in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        heap_data = [self._heap[i] for i in range(self._heap.length())]
        return 'HEAP ' + str(heap_data)

    def add(self, node: object) -> None:
        """
        Adds node to the heap. 
        """

        # If the node is empty 
        if self._heap.is_empty():
            self._heap.append(node)
            return

        self._heap.append(node)
        node_index = self._heap.length() - 1
        parent_index = (node_index - 1) // 2
        parent = self._heap[parent_index]

        # While parent node is larger than child, swap them
        while parent > node:
            temp = parent
            self._heap[parent_index] = node
            self._heap[node_index] = temp
            node_index = parent_index
            
            # When at the start of the heap
            if node_index == 0:
                return
            # Increment to continue
            else:
                parent_index = (node_index - 1) // 2
                parent = self._heap[parent_index]

    def is_empty(self) -> bool:
        """
        Returns True/False depending if empty/not empty.
        """
        if self._heap.length():
            return False
        else:
            return True

    def get_min(self) -> object:
        """
        Returns the min value (min node) of the heap. If heap is empty it raises an exception.
        """
        if self._heap.length():
            return self._heap[0]
        else:
            raise MinHeapException

    def remove_min(self) -> object:
        """
        Removes min node from the heap.
        """
        if self._heap.is_empty():
            raise MinHeapException
        return_value = self._heap[0]

        # If heap has one element
        if self._heap.length() == 1:
            self._heap.remove_at_index(0)
            return return_value

        # Last element value is now first
        self._heap[0] = self._heap[self._heap.length() - 1]
        # Deleting the last element
        self._heap.remove_at_index(self._heap.length() - 1)

        # If heap has only two elements
        if self._heap.length() == 2:
            if self._heap[0] > self._heap[1]:
                temp = self._heap[0]
                self._heap[0] = self._heap[1]
                self._heap[1] = temp
                return return_value
            
        # Once item deleted, we percolate the new min node
        _percolate_down(self._heap, 0)

        return return_value
    

    def build_heap(self, da: DynamicArray) -> None:
        """
        Builds heap from the given array.
        """

        # Creating the heap in the block
        self._heap = DynamicArray()
        for i in range(0, da.length()):
             self._heap.append(da[i])

        # If only two values in heap
        if self._heap.length() == 2:
            if self._heap[0] > self._heap[1]:
                self._heap[0], self._heap[1] = self._heap[1], self._heap[0]
                return
            
        # This is what we will pass to heapify
        node_to_check_index = (self._heap.length() // 2) - 1
        # Percolating till get to front of heap
        while node_to_check_index >= 0:
            _percolate_down(self._heap, node_to_check_index)
            node_to_check_index = node_to_check_index - 1
            

    def size(self) -> int:
        """
        Returns the sixe of the heap.
        """
        if self._heap.length():
            return self._heap.length()
        else:
            return 0

    def clear(self) -> None:
        """
        Clears the heap.
        """
        self._heap = DynamicArray()
    
  

def heapsort(da: DynamicArray) -> None:
    """
    Sorts the heap.
    """
    
    # Variable for length of array
    n = da.length()

    # Iterating through values and percolating. Reducing length passed to percolate. 
    for i in range(n // 2 - 1, -1, -1): 
       _percolate_down(da, i, n)  
    for i in range(n-1, 0, -1): 
        da[i], da[0] = da[0], da[i] 
        _percolate_down(da, 0, i)
    


def _percolate_down(da: DynamicArray, node_to_check_index: int, length=None) -> None:
    """
    Percolates the passed value down the passed array. Accepts optional third value for length. 
    """
    if length is None:
        da_length = da.length()
    else:
        da_length = length

    # While not at he head of the heap and not beyond array size
    while 0 <=node_to_check_index<da_length:
        child= None
        # Establishing children of node to be percolated down
        child_1_index = 2 * node_to_check_index + 1
        child_2_index = 2 * node_to_check_index + 2

        # Establishing the child that would be swapped and whether node needs to be swaped at all
        if child_2_index < da_length and da[child_2_index] < da[node_to_check_index]:
            if da[child_2_index] < da[child_1_index]:
                child = child_2_index
            else:
                child = child_1_index
        elif child_1_index < da_length and da[child_1_index] < da[node_to_check_index]:
            child = child_1_index

        # If no child we can stop percolation
        if child is None:
            return
        # Increment to continue the while loop (percolation)
        else:
            da[node_to_check_index], da[child] = da[child], da[node_to_check_index]
            node_to_check_index = child






# ------------------- BASIC TESTING -----------------------------------------

if __name__ == '__main__':

    # print("\nPDF - add example 1")
    # print("-------------------")
    # h = MinHeap()
    # print(h, h.is_empty())
    # for value in range(300, 200, -15):
    #     h.add(value)
    #     print(h)

    # print("\nPDF - add example 2")
    # print("-------------------")
    # h = MinHeap(['fish', 'bird'])
    # print(h)
    # for value in ['monkey', 'zebra', 'elephant', 'horse', 'bear']:
    #     h.add(value)
    #     print(h)

    # print("\nPDF - is_empty example 1")
    # print("-------------------")
    # h = MinHeap([2, 4, 12, 56, 8, 34, 67])
    # print(h.is_empty())

    # print("\nPDF - is_empty example 2")
    # print("-------------------")
    # h = MinHeap()
    # print(h.is_empty())

    # print("\nPDF - get_min example 1")
    # print("-----------------------")
    # h = MinHeap(['fish', 'bird'])
    # print(h)
    # print(h.get_min(), h.get_min())

    

    # print("\nPDF - remove_min example 1")
    # print("--------------------------")
    # h = MinHeap([-30425, -13996, -13996, 46328, -13920, 68374])
    # print(h, end=' ')
    # print(h.remove_min())
    # print(h, end=' ')



    # print("\nPDF - remove_min example 1")
    # print("--------------------------")
    # h = MinHeap([-7284, 5470, 82852, 82852, 88135])
    # print(h, end=' ')
    # print(h.remove_min())
    # print(h, end=' ')

    # print("\nPDF - remove_min example 1")
    # print("--------------------------")
    # h = MinHeap(['NoMYY', 'QHDqUDE', 'kQ', 'Rh_ESJQK', 'fkxT'])
    # print(h, end=' ')
    # print(h.remove_min())
    # print(h, end=' ')

    # print("\nPDF - remove_min example 1")
    # print("--------------------------")
    # h = MinHeap([1, 10, 2, 9, 3, 8, 4, 7, 5, 6])
    # while not h.is_empty() and h.is_empty() is not None:
    #     print(h, end=' ')
    #     print(h.remove_min())

    # print("\nPDF - build_heap example 1")
    # print("-------------------------")
    # da = DynamicArray([6567, 272, 3208, 42182, 76924, -24347, -87739, 43710, 76205])
    # h = MinHeap([])
    # correct = DynamicArray([-87739, 272, -24347, 42182, 76924, 6567, 3208, 43710, 76205])
    
    # # print(h)
   
    # h.build_heap(da)
    # print("------------------", h)
    # print(correct)



    # print("\nPDF - build_heap example 1")
    # print("--------------------------")
    # da = DynamicArray([46293, -62393, 38037, -36087, 33218, -15177, -3375, 25071, -85085, -59109])
    # h = MinHeap([])
    # correct = DynamicArray([-85085, 46293, -15177, -62393, -59109, 38037, -3375, 25071, -36087, 33218])
    
    # # print(h)
   
    # h.build_heap(da)
    # print("------------------", h)
    # print(correct)

    

    # print("\nPDF - build_heap example 1")
    # print("--------------------------")
    # da = DynamicArray([100, 20, 6, 200, 90, 150, 300])
    # h = MinHeap(['zebra', 'apple'])
    # print(h)
    # h.build_heap(da)
    # print(h)


    # print("--------------------------")
    # print("Inserting 500 into input DA:")
    # da[0] = 500
    # print(da)

    # print("Your MinHeap:")
    # print(h)
    # if h.get_min() == 500:
    #     print(
    #         "Error: input array and heap's underlying DA reference same object in memory"
    #     )

    print("\nPDF - heapsort example 1")
    print("------------------------")
    da = DynamicArray([100, 20, 6, 200, 90, 150, 300])
    print(f"Before: {da}")
    heapsort(da)
    print(f"After:  {da}")

    print("\nPDF - heapsort example 2")
    print("------------------------")
    da = DynamicArray(['monkey', 'zebra', 'elephant', 'horse', 'bear'])
    print(f"Before: {da}")
    heapsort(da)
    print(f"After:  {da}")

    # print("\nPDF - size example 1")
    # print("--------------------")
    # h = MinHeap([100, 20, 6, 200, 90, 150, 300])
    # print(h.size())

    # print("\nPDF - size example 2")
    # print("--------------------")
    # h = MinHeap([])
    # print(h.size())

    # print("\nPDF - clear example 1")
    # print("---------------------")
    # h = MinHeap(['monkey', 'zebra', 'elephant', 'horse', 'bear'])
    # print(h)
    # print(h.clear())
    # print(h)
