# Factors while choosing a sorting algorithm:
# - Size of data: Data can be large (size > 30) or small(size ~ 30)
# - Randomness of data: is data completely random, partially sorted or almost sorted?
# - Time and Space complexity:
# - Stability: will it retain the relative order of equal elements in the data?

# Sorting Algorithms:

# Normal Sorting Algorithms:
# 1. Bubble Sort:
# - Size of data: Suitable for small data
# - Randomness of data: Suitable when data is almost sorted.
# - Time and Space complexity:
# -- Time[Worst - O(n^2), Avg - , Best - O(n)]
# -- Space[]
# - Stability:
# Advantages:
# -

# 2. Insertion Sort:
# - Size of data: Suitable for small data
# - Randomness of data: Suitable when data is almost sorted.
# - Time and Space complexity:
# -- Time[Worst - O(n^2), Avg - , Best - O(n)]
# -- Space[]
# - Stability:
# Advantages:
# -

# 3. Selection Sort:
# - Size of data: Suitable for small data
# - Randomness of data: Suitable when data is almost sorted.
# - Time and Space complexity:
# -- Time[Worst - O(n^2), Avg - , Best - O(n^2)]
# -- Space[]
# - Stability:
# Advantages:
# - It retains first k smallest/largest elements in its first k iterations/passes. So we can use this property when we have to paginate our sorted data.

# Optimized Sorting Algorithms:
# 4. Merge Sort: Divide and Conquer Algorithm (Divide + Conquer + Combine)
# - Size of data: Suitable for large data
# - Randomness of data:
# - Time and Space complexity:
# -- Time[Worst - O(nlogn), Avg - O(nlogn), Best - O(nlogn)]
# -- Space[Worst - O(n), Avg - O(n), Best - O(n)]
# - Stability: True
# Advantages:
# -

# 5. Quick Sort: Divide and Conquer Algorithm
# - Size of data: Suitable for large data and case where it never leads to worst case scenario.
# - Randomness of data:
# - Time and Space complexity:
# -- Time[Worst - O(n^2), Avg - O(nlogn), Best - O(nlogn)]
# -- Space[Worst - O(n), Avg - O(n), Best - O(n)]
# - Stability: False
# Advantages:
# -

# 6. Heap Sort: Binary Tree data structure
# - Size of data:
# - Randomness of data:
# - Time and Space complexity:
# -- Time[Worst - O(nlogn), Avg - O(nlogn), Best - O(nlogn)]
# -- Space[Worst - O(1), Avg - O(1), Best - O(1)]
# - Stability: False
# Advantages:
# -

# Miscellaneous Sorting Algorithms:
# - Counting Sort
# - Radix/Bucket Sort
# - Shell Sort

# Extra Info:
# C++ --> Uses Randomized Quick Sort
# Python --> Uses Tim Sort (Timsort is a hybrid stable sorting algorithm) = Merge Sort + Insertion Sort
