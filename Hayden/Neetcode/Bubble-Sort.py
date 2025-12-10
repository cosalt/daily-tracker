"""
Algorithm: Bubble Sort(/Sinking Sort)

Sources:
    - https://www.geeksforgeeks.org/dsa/bubble-sort-algorithm/

Description:
    Simplest sorting algorithm

    Works by repeatedly swapping 
    the adjacent cells if they are
    in the wrong order

    Sorts the array other several passes 

Examples:
    Example 1:
        Input: nums = [5, 6, 1, 3]

        1.
            i=0
            1.1 [5, 6, 1, 3]
                5 < 6, so we continue

            i=1
            1.2 [5, 6, 1, 3]
                6 > 1, so we swap elements
                [5, 1, 6, 3]

            i=2
            1.3 [5, 1, 6, 3]
                6 > 3, so we swap elements
                [5, 1, 3, 6]
        [5, 1, 3, 6]

        2. 
            i=0
            2.1 [5, 1, 3, 6]
                5 > 1, so we swap
                [1, 5, 3, 6]
            
            i=1
            2.2 [1, 5, 3, 6]
                5 > 3, so we swap
                [1, 3, 5, 6]
        [1, 3, 5, 6]

        3. 
            i=0
            2.1 [1, 3, 5, 6]
                1 < 3, so we continue
                [1, 3, 5, 6]
        [1, 3, 5, 6]


        Solved

        Output: [1, 3, 5, 6]

Outcome:
    Pros:
        - Easy to understand and impliment
        - Does not require any additional memory space
        - It is a stable sorting algorithm, values with same key value 
        retain relative order in output

    Cons:
        - Bubble sort has a complexity of O(n^2) very slow on large sets
        - Mostly used for academics to show examples of sorting


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


# Main implimentations for the bubble sort algorithms

class bubbleSort:
    def bubbleSort(self, arr):
        n = len(arr)

        # Traverse all array elements
        for i in range(n):
            swapped = False

            # Last i element already in place
            # Traverse array from 0 to n-i-1
            for j in range(0, n-i-1):

                if (arr[j] > arr[j+1]):
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    swapped = True
                
            if (swapped == False):
                break


# Benchmarking the algorithms

# Bubble Sort (Iterative)
print("#########################")
start = timer()
bubbleSort().bubbleSort(items)
print("Bubble Sort (Iterative): ", items)
end = timer()
print("Execution time: ", end - start, "seconds")
print("#########################")
