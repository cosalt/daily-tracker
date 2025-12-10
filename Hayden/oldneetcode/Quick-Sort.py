"""
Algorithm: Quick Sort

Sources: 
    - https://www.geeksforgeeks.org/dsa/quick-sort-algorithm/
    - https://www.w3schools.com/dsa/dsa_algo_quicksort.php

Description:
    Picks an element as a pivot and 
    partitions the given array around 
    the picked pivot by placing the 
    pivot in its correct position
    in the sorted array.

    Chooses a Pivot (first element, 
    last element, random element, median)
    
    Partition the Array: arrange the array
    around the pivot, after partitioning
        - All elements smaller in left array of pivot
        - All elements greater in right array of pivot
        - Pivot is then in correct index 
        - Obtain the index of pivot
    
    Recursively Call: recursively apply process
    to the two seperate sub-arrays (left & right
    of pivot)

    Base Case: The recursion stop when there is 
    only one element left in the sub-arrays

Examples:
    Example 1:
        Input: nums = [4, 3, 1, 2, 5, 9, 7, 10, 6]

        1. [4, 3, 1, 2, |5|, 9, 7, 10, 6] # Pivot index = 4
            Move element to index 0 of its sub-array
            - 4, 3, 1, 2 < 5 (left)
            - 9, 7, 10, 6 > 5 (right)
            [[4, 3, 1, 2], |5|, [9, 7, 10, 6]]

        2. 
            2.1 [[4, |3|, 1, 2], ...] # Pivot index = 1
                - 1, 2 < 3 (left)
                - 4 > 3 (right)
                [[1, 2], |3|, [4]]

                2.1.1 [|1|, 2] # Pivot index = 0
                    - _ < 1 (left)
                    - 2 > 1 (right)
                    [|1|, [2]]
                
                2.1.2 [|4|] # Pivot index = 0
                2.1.3 [|2|] # Pivot index = 0

            [|1|, |2|, |3|, |4|, ...]
            
            2.2 [[..., [9, |7|, 10, 6]]] # Pivot index = 1
                - 6 < 7 (left)
                - 9, 10 > 7 (right)
                [[6], |7|, [9, 10]]

                2.2.1 [|6|] # Pivot index = 0

                2.2.2 [|9|, 10] # Pivot index = 0
                    - _ < 9 (left)
                    - 10 > 9 (right)
                    [|9|, [10]]
                
                2.2.3 [|10|] # Pivot index = 0
            
            [..., |6|, |7|, |9|, 10|]

        [|1|, |2|, |3|, |4|, |5|, |6|, |7|, |9|, |10|]        

        Solved

        Output: [1, 2, 3, 4, 5, 6, 7, 9, 10]

Outcome:
    Pros:
        - Divide and conquer
        - Efficient on large data sets
        - Low overhead
        - Cache friendly
        - "Fastest general purpose array"
        - Tail recursive, can utilise "tail call optimisation"

    Cons:
        - Worst case of O(n^2), badly chosen pivot
        - Not good for smaller sets
        - Not STABLE, if 2 elements have the same key their relative
        order will not be preserved


Time & Space Complexity:
    Time:
        Best:    O(n log(n))

        Average: O(n log(n))

        Worst:   O(n^2)


    Space:
        Best:    O(log n)

        Worst:   O(n)

"""


# Imports
from timeit import default_timer as timer


# Global input which all solutions use
items = list(map(int, input("Enter numbers separated by space: ").split()))


# Main implimentations for the quick sort algorithm

class quickSort:
    # Calls itself if sub-array size larger than 1
    def quickSort(self, array, low = 0, high = None):
        """Recursive Algorithm"""
        
        if high is None:
            high = len(array) - 1
        
        if low <= high:
            pivot_index = self.partition(array, low, high)
            self.quickSort(array, low, pivot_index-1)
            self.quickSort(array, pivot_index+1, high)

    # Recieves sub-array, moves values arround and swaps the pivot
    # Element into the sub-array and returns the index where the
    # next split in sub-arrays happens
    def partition(self, array, low, high):
        # Choose pivot 
        pivot = array[high]
        i = low - 1

        # Loops through index low to high comparing value to pivot
        # if less than or equal to, increment i and 
        # swap array[i] and array[j] without need for temp variable 
        for j in range(low, high):
            if (array[j] < pivot):
                i += 1
                array[i], array[j] = array[j], array[i]

        # 
        array[i+1], array[high] = array[high], array[i+1]

        return i+1
    

# Benchmarking the algorithms

# Quick Sort
print("#########################")
start = timer()
quickSort().quickSort(items)
print("Quick Sort: ", items)
end = timer()
print("Execution time: ", end - start, "seconds")
print("#########################")
