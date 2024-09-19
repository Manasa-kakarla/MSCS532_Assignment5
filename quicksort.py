def quicksort(arr):
    """Sorts the array using the Quicksort algorithm."""
    if len(arr) <= 1:
        return arr
    else:
        # Choosing the pivot (here we use the last element)
        pivot = arr[-1]
        # Partitioning the array into left (<= pivot) and right (> pivot)
        left = [x for x in arr[:-1] if x <= pivot]
        right = [x for x in arr[:-1] if x > pivot]
        
        # Recursively sorting the subarrays and combining results
        return quicksort(left) + [pivot] + quicksort(right)

# Example usage
if __name__ == "__main__":
    sample_array = [10, 7, 8, 9, 1, 5]
    sorted_array = quicksort(sample_array)
    print("Sorted array:", sorted_array)
