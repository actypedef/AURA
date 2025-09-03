"""
Write a function to find the median of two sorted lists of same size.
assert get_median([1, 12, 15, 26, 38], [2, 13, 17, 30, 45], 5) == 16.0
"""
def get_median(arr1, arr2, n):
    # Initialize variables for binary search
    low = 0
    high = n
    
    while low <= high:
        partitionX = (low + high) // 2
        partitionY = n - partitionX
        
        # Edge cases for partitioning
        maxX = float('-inf') if partitionX == 0 else arr1[partitionX - 1]
        minX = float('inf') if partitionX == n else arr1[partitionX]
        
        maxY = float('-inf') if partitionY == 0 else arr2[partitionY - 1]
        minY = float('inf') if partitionY == n else arr2[partitionY]
        
        # Check if partitions are correct
        if maxX <= minY and maxY <= minX:
            if (n % 2 == 0):
                return (max(maxX, maxY) + min(minX, minY)) / 2.0
            else:
                return max(maxX, maxY)
        elif maxX > minY:
            high = partitionX - 1
        else:
            low = partitionX + 1

# Test the function with the provided test case
assert get_median([1, 12, 15, 26, 38], [2, 13, 17, 30, 45], 5) == 16.0