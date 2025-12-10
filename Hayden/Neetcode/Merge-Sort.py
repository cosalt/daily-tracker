"""
Algorithm: Merge Sort

Sources:
    - https://en.wikipedia.org/wiki/Merge_sort

Description:
    The data is repeatedly split in 
    half until each item is its own list.

    Adjacent lists are then merged back
    together, with each item in the sub-list
    being entered in its correct sorted 
    position.

Examples:
    Example 1:
        Input: nums = [3, 3, 1, 5, 2, 3, 4, 4, 2]

        1. [3, 3, 1, 5, 2, 3, 4, 4, 2, 7, 1, 9]
        2. [[3, 3, 1, 5, 2, 3], [4, 4, 2, 7, 1, 9]]
        3. [[3, 3, 1], [5, 2, 3], [4, 4, 2], [7, 1, 9]]
        4. [[3], [3, 1], [5], [2, 3], [4], [4, 2], [7], [1, 9]]
        5. [[3], [3], [1], [5], [2], [3], [4], [4], [2], [7], [1], [9]]

        Every item is now its own list

        1.[[3], [3], [1], [5], [2], [3], [4], [4], [2], [7], [1], [9]]
        2.[[3, 3], [1, 5], [2, 3], [4, 4], [2, 7], [1, 9]]
        3.[[1, 3, 3, 5], [2, 3, 4, 4], [1, 2, 7, 9]]
        4.[[1, 2, 3, 3, 3, 4, 4, 5], [1, 2, 7, 9]]
        5.[1, 1, 2, 2, 3, 3, 3, 4, 4, 5, 7, 9]

        Solved

        Output: [1, 1, 2, 2, 3, 3, 3, 4, 4, 5, 7, 9]

Outcome:
    Pros:
        - Consistent Performance
        - Stable Sorting
        - Efficient for large datasets
        - Parallelisable (nature of divide and conquer)
        - Suitable for external sorting

    Cons:
        - Space Complexity high
        - Not In-Place
        - Slower for small datasetes
        - Recursive Overhead
        - Complex implimentation


Time & Space Complexity:
    Time:
        Best:    O(n log(n))

        Average: O(n log(n))

        Worst:   O(n log(n))


    Space:
        Worst:   O(n)

"""

# Imports
from timeit import default_timer as timer


# Global input which all solutions use
items = list(map(int, input("Enter numbers separated by space: ").split()))


# Main implimentations for the merge sort algorithm
class mergeSortTopDown:
    """Recursive algorithm"""
    def mergeSort(self, l):
        # A list of 0 or 1 elements is sorted by default
        if len(l) <= 1:
            return l
        
        
        # Divide the list into equal size sub-lists
        # left = first half, right = second half
        
        left, right = [], []

        for i, v in enumerate(l):
            if i < (len(l))//2:
                left.append(v)
            else:
                right.append(v)
        
        left, right = self.mergeSort(left), self.mergeSort(right)

        return self.merge(left, right)
    
    def merge(self, left, right):
        result = []

        # Checks if left and right are not empty
        while (left) and (right):
            # Compares element 1 of left and right, smaller element appends to result
            if left[0] <= right[0]:
                result.append(left[0])
                left = left[1:]
            else:
                result.append(right[0])
                right = right[1:]
        
        # Checks for remaining elements
        while (left):
            result.append(left[0])
            left = left[1:] 
        while (right):
            result.append(right[0])
            right = right[1:]
        
        return result


# Benchmarking the algorithms

# Top-down
print("#########################")
start = timer()
print("Top-down merge sort: ", mergeSortTopDown().mergeSort(items))
end = timer()
print("Execution time: ", end - start, "seconds")
print("#########################")
