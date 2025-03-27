def quicksort(arr, low=0, high=None):
    """
    Implementation of quicksort algorithm.
    
    Args:
        arr: List to be sorted
        low: Starting index of the array
        high: Ending index of the array
        
    Returns:
        Sorted list
    """
    if high is None:
        high = len(arr) - 1

    # Base condition for recursion
    if low < high:
        # Find the partition index
        pivot_index = partition(arr, low, high)
        
        # Recursively sort the sublists
        quicksort(arr, low, pivot_index - 1)
        quicksort(arr, pivot_index + 1, high)
    
    return arr


def partition(arr, low, high):
    """
    Partition the array and return the pivot index.
    
    Args:
        arr: List to be partitioned
        low: Starting index of the segment
        high: Ending index of the segment
        
    Returns:
        The position of the pivot after partitioning
    """
    # Select the pivot (in this case, we are selecting the last element as pivot)
    pivot = arr[high]
    i = low - 1  # Index of smaller element
    
    # Traverse through the array and rearrange elements
    for j in range(low, high):
        if arr[j] < pivot:  # If current element is smaller than pivot
            i += 1  # Increment the index of smaller element
            swap(arr, i, j)
    
    # Place the pivot in its correct position
    swap(arr, i + 1, high)
    return i + 1  # Return the pivot index


def swap(arr, i, j):
    """
    Helper function to swap two elements in an array.
    
    Args:
        arr: List containing elements to swap
        i: Index of first element
        j: Index of second element
    """
    arr[i], arr[j] = arr[j], arr[i]


def is_sorted(arr):
    """
    Helper function to check if an array is sorted.
    
    Args:
        arr: List to check
        
    Returns:
        True if the list is sorted, False otherwise
    """
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True
