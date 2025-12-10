"""
Algorithm: Heap Sort

Sources:
    - https://en.wikipedia.org/wiki/Heapsort
    - https://en.wikipedia.org/wiki/Binary_heap#Building_a_heap

Description:
    Heap sort is an efficent
    comparison based sorting
    algorithm.

    Reorganises an input array
    into a heap - (a data structure
    where each node is greater than
    its children) then repeatedly
    removes the largest node from the
    heap placing it at the end of array

    The heapsort algorithm can be split
    into two phases:
        Heap Construction (array of n elements):
            Williams' Method:
                - Start with an empty heap.
                - Sucessively inserting each element from array.
                - O(n log(n)).
            
            W.Floyd Method:
                - Starts arbritrarily putting elements on a binary tree.
                - Starting from the lowest level moving upwards.
                - sift the root of each subtree downaward as in the deletion 
                algorithm until the heap property is restored.  

        Heap Extraction:
            Heap is coverted into a sorted array by moving the largest
            element from the root of the heap and placing it at the start
            of the array, updating the heap after each removal.
            Once all objects remvoed form the heap the array is sorted.

Notes:
    - Convert array to a max heap - `heapify`
    - Delete the root node of max heap, replace it with last node and heapify
    - repeate while size of heap > 1

Examples:
    Example 1:
        Index:         0, 1, 2, 3, 4,  5, 6
        Input: nums = [9, 4, 3, 8, 10, 2, 5]

        Heap Construction:
            ---
             9
            / \
           /   \            Compare each node with its children, ensuring
          /     \           parent nodes are larger. This causes smaller nodes
         /       \          to bubble down and larger nodes to rise to top
         4        3         Start with leaf nodes
       / \       / \
      /   \     /   \
    |8|  |10|  |2|  |5|
   
            [9, 4, 3, |8|, |10|, |2|, |5|]
            ---

             9
            / \
           /   \            Then look at the next upper level
          /     \
         /       \
       |4|       |3|
       / \       / \
      /   \     /   \
      8    10   2    5

            [9, |4|, |3|, 8, 10, 2, 5]
            ---

             9                  9
            / \                / \
           /   \              /   \         Node 4 is smaller than its child node (10)
          /     \            /     \        So swap it with the larger child to maintain
         /       \    ->    /       \       the property that a parent should be larger than
       |4|        3       |10|       3       its children
       / \<-swap / \      / \       / \
      /   \     /   \    /   \     /   \
    |8|  |10|   2    5   8   |4|  2     5
    8 < 10, 10 largest child
    4 < 10 swap with largest child

            [9, |4|, 3, 8, |10|, 2, 5]
                 ^----------^
                     swap
            [9, |10|, 3, 8, |4|, 2, 5]
            ---

             9                   9
            / \                 / \
           /   \               /   \         Check for the next node (3) in current level, since
          /     \             /     \        it has a larger child, so swap it to insure parent 
         /       \    ->     /       \       has larger value
        10       |3|        10       |5|       
       / \       / \ <-swap/ \       / \
      /   \     /   \     /   \     /   \
     8    4   |2|   |5|  8     4  2     |3|
     2 < 5, 5 largest child
     3 < 5, swap with largest child

            [9, 10, |3|, 8, 4, 2, |5|]
                     ^-------------^
                          swap
            [9, 10, |5|, 8, 4, 2, |3|]
    [9, |10|, |5|, |8|, |4|, |2|, |3|]
    We now have two smaller valid max heaps
            ---

            Now the root

            |9|                 |10|
            / \                 / \
     swap->/   \               /   \        Node 9 is smaller than its child node (10), so
          /     \             /     \       swap it with its larger child to maintain the 
         /       \    ->     /       \      property that the parent should be larger than 
       |10|      |5|       |9|        5     its children       
       / \       / \       / \       / \
      /   \     /   \     /   \     /   \
     8    4    2     3   8     4  2      3
     10 > 5, 10 largest child
     9 < 10, swap with largest child

            [|9|, |10|, 5, 8, 4, 2, 3]
              ^----^
               swap
            [|10|, |9|, 5, 8, 4, 2, 3]
     [10, 9, 5, 8, 4, 2, 3]
     we now have a max heap built
        #########################################################################
        Heap Extraction:
                ---
            |10|                 |3|
            / \\                 / \
           /   \\<-swap         /   \           Swap the maximum element(10) with the 
          /     \\             /     \          last element(3) in the unsorted array
         /       \\    ->     /       \         Decrease the size of the heap by 1
        9         5\        |9|        5        (ignore the last element as it is sorted)
       / \       / \\       / \       / \
      /   \     /   \\     /   \     /   \
     8    4    2    |3|   8     4   2   |10|
[|10|, 9, 5, 8, 4, 2, |3|] [|3|, 9, 5, 8, 4, 2, |10|]
  ^--------------------^                         ✓
          swap
                ---

                 |3|                   9
                 / \                  / \
          swap->/   \                /   \           Now, root the violate the max-heap property 
               /     \              /     \          so heapify it
              /       \     ->     /       \         swap node 3 with its largest child (9)
            |9|        5         |3|        5        still node 3 will have larger children so swap it
            / \       / \        / \       / \       with largest one (node 8)
           /   \     /   \swap->/   \     /   \      5 < 9, 9 largest child, 3 < 9 swap with largest child
          8    4    2   (10)  |8|    4   2   (10)    4 < 8, 8 largest child, 3 < 8 swap with largest child
|[3|, |9|, 5, 8, 4, 2, (10)] [9, |3|, 5, |8|, 4, 2, (10)]
  ^----^                ✓         ^------^           ✓
   swap                             swap
                ---
                 |9|                  |2|
                 /|\                  / \
                / | \                /   \           Now, we have a max heap. swap the maximum
               / s|  \              /     \          element(9) with the last element(2) in the 
              /  w|   \     ->     /       \         unsorted array, then decrease heap size by 1
             8   a|    5          8         5        (ignoring the second last element as sorted)
            / \  p|   / \        / \       / \       
           /   \  \  /   \      /   \     /   \      
          3    4   |2|   (10)  3     4  |9|   (10)    
||9|, 8, 5, 3, 4, |2|, (10)] [|2|, 8, 5, 3, 4, |9|, (10)]
  ^----------------^    ✓                       ✓    ✓
         swap
                ---
                
                 |2|                  |8|
                 / \                  / \
          swap->/   \                /   \           Now, root violate max-heap property, so heapify  
               /     \              /     \          it. Swap node 2 with its largest child(8)
              /       \     ->     /       \         still node 2 has larger children, so swap it with
            |8|        5         |2|        5        largest one (node 4)
            / \       / \        / \<-swap / \       
           /   \     /   \      /   \     /   \      5 < 8, 8 largest child, 2 < 8 swap with largest child
          3    4    (9)   (10) 3    |4| (9)   (10)    3 < 4, 4 largest child, 2 < 4 swap with largest child
|[2|, |8|, 5, 3, 4, (9), (10)] [8, |2|, 5, 3, |4|,  (9), (10)]
  ^----^             ✓    ✓         ^---------^     ✓    ✓
   swap                                 swap
                ---

                 |8|                  |2|
                 /|\                  / \
                / | \                /   \           Now, we have a max heap. swap the maximum
               / s|  \              /     \          element(8) with the last element(2) in the 
              /  w|   \     ->     /       \         unsorted array, then decrease heap size by 1
             4   a|    5          4         5        (ignoring the second last element as sorted)
            / \  p|   / \        / \       / \       
           /   \  /  /   \      /   \     /   \      
          3    |2|  (9)   (10) 3    |8|  (9)   (10)    
|[8|, 4, 5, 3, |2|, (9), (10)] [2, 4, 5, 3, (8), (9), (10)]
  ^-------------^    ✓    ✓                 ✓    ✓    ✓
        swap
                ---
                Repeat these steps until the problem is solved
        Solved

        Output: [2, 3, 4, 5, 8, 9, 10]

Outcome:
    Pros:
        - Efficient time complexity (o log(n))
        - Memory usage: Memory usage is minimal as process is iterative rather than recursive
        - Simplicity: It is simpler to understand than other equally efficient algorithms
    
    Cons:
        - Costly: Constants are higher compared to merge sort even if they have the same time complexity
        - Unstable: Heap sort is unstable and might rearange relative order
        - Inefficient: high constraints in the time complexity

Time & Space Complexity:
    Time:
        Best:       O(n log(n))

        Average:    O(n log(n))

        Worst:      O(n log(n))


    Space:
        Worst:      0(1)
        
"""


# Imports
from timeit import default_timer as timer


# Global input which all solutions use
items = list(map(int, input("Enter numbers separated by space: ").split()))


# Main implimentations for the heap sort algorithm

class heapSort:
    
    # Helper function 
    # Heapify subtree rooted with node i (index in arr[])
    def heapify(self, arr, n, i):
        # Intialise largest element as root
        largest = i

        # Left index = (2*i) + 1
        # Right index = (2*i) + 2
        l, r = (2 * i) + 1, (2 * i) + 2

        # If (left) child is larger than root
        if (l < n) and (arr[l] > arr[largest]):
            # Then swap
            largest = l
        
        # If (right) child is larger than largest so far
        if (r < n) and (arr[r] > arr[largest]):
            # Then swap
            largest = r

        # If largest is not root
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i] # Swap

            # Recursively heapify affected sub-tree
            self.heapify(arr, n, largest)


    def heapSort(self, arr):
        n = len(arr)

        # Build heap (rearrange array)
        for i in range(((n // 2) -1), -1, -1):
            self.heapify(arr, n, i)

        # One by one extract element from heap
        for i in range((n - 1), 0, -1):
            # Move root to end
            arr[0], arr[i] = arr[i], arr[0]

            # Call max-heapify on the reduced heap
            self.heapify(arr, i, 0)
    

# Benchmarking the algorithms

# Heap Sort
print("#########################")
start = timer()
heapSort().heapSort(items)
print("Heap Sort: ", items)
end = timer()
print("Execution time: ", end - start, "seconds")
print("#########################")
