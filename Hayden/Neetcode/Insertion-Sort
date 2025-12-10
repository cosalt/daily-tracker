"""
Algorithm: Insertion Sort

Sources:
    - https://www.geeksforgeeks.org/dsa/insertion-sort-algorithm/

Description:
    Insertion sort is a simple sorting
    algorithm that works by iteratively
    inserting each element of an unsorted
    list into its correct position

    Two groups sorted and unsorted
    you pick a element from the unsorted group
    then place it into the right position

Examples:
    Example 1:
        Input: nums = [12, 11, 13, 5, 6]

        
        key = 11
        1. [12|, 11, 13, 5, 6]
            Compare key - 11 with 12
            12 in wrong order shift to right to
            make space for key
            [11|, 12, 13, 5, 6]
        
        key = 13
        2. [11, 12|, 13, 5, 6]
            Compare key - 13 with 12
            12 in correct order so continue
            [11, 12, 13|, 5, 6]
        
        key = 5
        3. [11, 12, 13|, 5, 6]
            Compare key with all elements in 
            sorted sub-array starting with 13,
            if element wrong shift to right
            [5, 11, 12|, 13, 6] 

        key = 6
        4. [5, 11, 12, 13|, 6]
            Compare key with all elements
            in sorted sub-array starting with 13,
            if element wrong shoft to right
            [5, 6, 11, 12|, 13]
        
        5. [5, 6, 11, 12|, 13]
            The sorted sub-array contains whole array,
            Means whole array is sorted
            [5, 6, 11, 12, 13|]
        
        [5, 6, 11, 12, 13]

        Solved

        Output: [5, 6, 11, 12, 13]

Outcome:
    Pros:
        - Simple and easy to impliment
        - Stable sorting algorithm
        - Efficient for small lists and nearly sorted lists
        - Space-efficient as its in place algorithm

    Cons:
        - Inefficient for larger lists
        - Not as efficient as other algorithms


Time & Space Complexity:
    Time:
        Best:       O(n)

        Average:    O(n^2)

        Worst:      O(n^2)


    Space:
        Worst:      O(1)
        
"""

# Imports
from timeit import default_timer as timer


# Global input which all solutions use
items = list(map(int, input("Enter numbers separated by space: ").split()))


# Main implimentations for the insertion sort algorithms

class insertionSort:
    def insertionSort(self, arr):
        for i in range(1, len(arr)):
            # Element in current index
            key = arr[i]
            j = i-1

            # Move elements of sorted array that
            # are greater than key, 1 position right
            while (j >= 0) and (key < arr[j]):
                arr[j+1] = arr[j]
                j -= 1
            arr[j+1] = key


# Benchmarking the algorithms

# Insertion Sort (Iterative)
print("#########################")
start = timer()
insertionSort().insertionSort(items)
print("Insertion Sort (Iterative): ", items)
end = timer()
print("Execution time: ", end - start, "seconds")
print("#########################")
