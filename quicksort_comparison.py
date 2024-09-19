import random
import time

def deterministic_quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[-1]
    left = [x for x in arr[:-1] if x <= pivot]
    right = [x for x in arr[:-1] if x > pivot]
    return deterministic_quicksort(left) + [pivot] + deterministic_quicksort(right)

def randomized_quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot_index = random.randint(0, len(arr) - 1)
    pivot = arr[pivot_index]
    left = [x for i, x in enumerate(arr) if x <= pivot and i != pivot_index]
    right = [x for i, x in enumerate(arr) if x > pivot]
    return randomized_quicksort(left) + [pivot] + randomized_quicksort(right)

def time_sort(sort_function, arr):
    start_time = time.time()
    sort_function(arr)
    end_time = time.time()
    return end_time - start_time

def generate_sorted_array(size):
    return list(range(size))

def generate_reverse_sorted_array(size):
    return list(range(size, 0, -1))

def generate_random_array(size):
    return [random.randint(0, size) for _ in range(size)]

def run_tests():
    sizes = [100, 1000, 5000, 10000]
    
    for size in sizes:
        print(f"\nArray Size: {size}")

        # Random array
        random_array = generate_random_array(size)
        print("Random Array:")
        det_time = time_sort(deterministic_quicksort, random_array.copy())
        rand_time = time_sort(randomized_quicksort, random_array.copy())
        print(f"Deterministic Quicksort Time: {det_time:.6f} seconds")
        print(f"Randomized Quicksort Time: {rand_time:.6f} seconds")

        # Sorted array
        sorted_array = generate_sorted_array(size)
        print("Sorted Array:")
        det_time = time_sort(deterministic_quicksort, sorted_array.copy())
        rand_time = time_sort(randomized_quicksort, sorted_array.copy())
        print(f"Deterministic Quicksort Time: {det_time:.6f} seconds")
        print(f"Randomized Quicksort Time: {rand_time:.6f} seconds")

        # Reverse-sorted array
        reverse_sorted_array = generate_reverse_sorted_array(size)
        print("Reverse Sorted Array:")
        det_time = time_sort(deterministic_quicksort, reverse_sorted_array.copy())
        rand_time = time_sort(randomized_quicksort, reverse_sorted_array.copy())
        print(f"Deterministic Quicksort Time: {det_time:.6f} seconds")
        print(f"Randomized Quicksort Time: {rand_time:.6f} seconds")

if __name__ == "__main__":
    run_tests()
