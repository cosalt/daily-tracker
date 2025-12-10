"""
Algorithm: Tim Sort

Sources:
    - https://en.wikipedia.org/wiki/Timsort
    - https://www.geeksforgeeks.org/dsa/tim-sort-in-python/

Description:
    TimSort is a derivitive hybrid of Merge Sort and
    Tim Sort.(Used in .sort() and sorted() until
    python 3.11)

    The algorithm finds subsequences of data already
    ordered (runs) and uses them to sort the remainder
    more efficiently.

    Basically divide and conquer then use Tim sort
    on sub arrays and merge.

Examples:
    Example 1:
        Input: nums = [4, 0, 12, 35, 89, 56, 3, 30, 12, 5, 64, 55, 29, 17, 1, 2, 3, 4, 5, 33, 7, 18, 26, 51, 63, 22, 844, 91, 73, 47]

        1. 
            Run size = 4
            [4, 0, 12, 35|, 89, 56, 3, 30|, 12, 5, 64, 55|, 29, 17, 1, 2|, 3, 4, 5, 33|, 7, 18, 26, 51|, 63, 22, 84, 91|, 73, 47]
            Tim Sorting:
                [0, 4, 12, 35],
                [3, 30, 56, 80],
                [5, 12, 55, 64],
                [1, 2, 17, 29],
                [3, 4, 5, 33],
                [7, 18, 26, 51],
                [22, 63, 84, 91],
                [47, 73]
            [0, 4, 12, 35|, 3, 30, 56, 80|, 5, 12, 55, 64|, 1, 2,17, 29|, 3, 4, 5, 33|, 7, 18, 26, 51|, 22, 63, 84, 91|, 47, 73]

        2.
            Run Size = 8
            [0, 4, 12, 35, 3, 30, 56, 80|, 5, 12, 55, 64, 1, 2,17, 29|, 3, 4, 5, 33, 7, 18, 26, 51|, 22, 63, 84, 91, 47, 73]
            Tim Sorting:
                [0, 3, 4, 12, 30, 35, 56, 80],
                [1, 2, 5, 12, 17, 29, 55, 64],
                [3, 4, 5, 7, 18, 26, 33, 51],
                [22, 47, 63, 73, 84, 91]
            [0, 3, 4, 12, 30, 35, 56, 80|, 1, 2, 5, 12, 17, 29, 55, 64|, 3, 4, 5, 7, 18, 26, 33, 51|, 22, 47, 63, 73, 84, 91]

        3.
            Run Size = 16
            [0, 3, 4, 12, 30, 35, 56, 80, 1, 2, 5, 12, 17, 29, 55, 64|, 3, 4, 5, 7, 18, 26, 33, 51, 22, 47, 63, 73, 84, 91]
            Tim Sorting:
                [0, 1, 2, 3, 4, 5, 12, 12, 17, 29, 30, 35, 55, 56, 64, 80],
                [3, 4, 5, 7, 18, 22, 26, 33, 47, 51, 63, 73, 84, 91]
            [0, 1, 2, 3, 4, 5, 12, 12, 17, 29, 30, 35, 55, 56, 64, 80|, 3, 4, 5, 7, 18, 22, 26, 33, 47, 51, 63, 73, 84, 91]

        4.
            Run Size = 32
            [0, 1, 2, 3, 4, 5, 12, 12, 17, 29, 30, 35, 55, 56, 64, 80, 3, 4, 5, 7, 18, 22, 26, 33, 47, 51, 63, 73, 84, 91]
            Tim Sorting:
                [0, 1, 2, 3, 4, 5, 12, 12, 17, 29, 30, 35, 55, 56, 64, 80, 3, 4, 5, 7, 18, 22, 26, 33, 47, 51, 63, 73, 84, 91]
            [0, 1, 2, 3, 3 ,4 ,4 5, 5, 7, 12, 12, 17, 18, 22, 26, 29, 30, 33, 35, 47, 51, 55, 56, 63, 64, 73, 80, 84, 91]
        [0, 1, 2, 3, 3 ,4 ,4 5, 5, 7, 12, 12, 17, 18, 22, 26, 29, 30, 33, 35, 47, 51, 55, 56, 63, 64, 73, 80, 84, 91]


        Solved

        Output: [0, 1, 2, 3, 3 ,4 ,4 5, 5, 7, 12, 12, 17, 18, 22, 26, 29, 30, 33, 35, 47, 51, 55, 56, 63, 64, 73, 80, 84, 91]


Outcome:
    Pros:
        - Very good at sorting lists that are partially sorted
        - Stable sorting algorithm
        - Easy to understand as its a hybrid of merge and Tim

    Cons:
        - High space complexity as it is not an in-place sort
        - Slightly slower on random data as its designed for real world
        data that incudes trends or partially sorted lists


Time & Space Complexity:
    Time:
        Best:       O(n)

        Average:    O(n log(n))

        Worst:      O(n log(n))


    Space:
        Worst:      O(n)
        
"""

# Imports
from timeit import default_timer as timer


# Global input which all solutions use
items = list(map(int, input("Enter numbers separated by space: ").split()))


# Main implimentations for the tim sort algorithms

class timSort:
    def insertionSort(self, arr, left=0, right=None):
        # Base case (already sorted)
        if right is None:
            right = len(arr) - 1

        for i in range(left + 1, right + 1):
            # Element in current index
            key = arr[i]
            j = i-1

            # Move elements of sorted array that
            # are greater than key, 1 position right
            while (j >= left) and (key < arr[j]):
                arr[j+1] = arr[j]
                j -= 1
            arr[j+1] = key

        return arr
    
    def merge(self, left, right):
        # If left subarray empty, return right array
        if not left: return right
        # If Right subarray empty, return left array
        if not right: return left

        # Compare the first elements of the 2 subarrays
        if (left[0] < right[0]): return [left[0]] + self.merge(left[1:], right)
        else: return [right[0]] + self.merge(left, right[1:])
        
    
    def timSort(self, arr):
        # Initialise minimum run size
        minRun = 32
        n = len(arr)

        # Traaverse the array and do insertion sort on each subarray of size minRun
        for i in range(0, n, minRun):
            self.insertionSort(arr, i, min(i + minRun - 1, (n - 1)))
        
        size = minRun
        while (size < n):
            #Divide array into merge size
            for start in range(0, n, size*2):
                # Find midpoint and endpoint of left and right subarrays
                midpoint = start + size
                end = min((start + size * 2 - 1), (n - 1))

                # Merge the two subarrays
                mergedArray = self.merge(arr[start:midpoint], arr[midpoint:end + 1])

                arr[start:start + len(mergedArray)] = mergedArray
            size *= 2

        return arr
    

# Benchmarking the algorithms

# Tim Sort 
print("#########################")
start = timer()
timSort().timSort(items)
print("Tim Sort: ", items)
end = timer()
print("Execution time: ", end - start, "seconds")
print("#########################")
