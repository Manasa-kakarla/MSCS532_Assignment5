import random

def randomized_quicksort(arr):
    """Sorts the array using the randomized Quicksort algorithm."""
    if len(arr) <= 1:
        return arr
    else:
        # Randomly select a pivot
        pivot_index = random.randint(0, len(arr) - 1)
        pivot = arr[pivot_index]
        
        # Partitioning the array into left (<= pivot) and right (> pivot)
        left = [x for i, x in enumerate(arr) if x <= pivot and i != pivot_index]
        right = [x for i, x in enumerate(arr) if x > pivot]
        
        # Recursively sorting the subarrays and combining results
        return randomized_quicksort(left) + [pivot] + randomized_quicksort(right)

# Example usage
if __name__ == "__main__":
    sample_array = [25, 4, 30, 54, 6, 41]
    sorted_array = randomized_quicksort(sample_array)
    print("Sorted array:", sorted_array)
