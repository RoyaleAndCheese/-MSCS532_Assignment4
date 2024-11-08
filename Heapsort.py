import random
import time

def heapify(arr, n, i):
    # Largest element is the root
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    # Check if left child exists and is greater than the root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Check if right child exists and is greater than the root
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If the largest element is not the root, swap and heapify the affected subtree
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heapsort(arr):
    n = len(arr)

    # Create a max-heap 
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements from the heap one by one
    for i in range(n - 1, 0, -1):
        # Move current root to the end
        arr[i], arr[0] = arr[0], arr[i]
        # Call heapify on the reduced heap
        heapify(arr, i, 0)


# Example
arr = [22, 15, 23, 9, 2, 5]
heapsort(arr)
print("Sorted array is:", arr)


# Edge Case 4: Already sorted array
def generate_sorted_array(size, start_value=1, step=1):
    # Generate a sorted array with `size` elements, starting from `start_value`, increasing by `step`
    return [start_value + i * step for i in range(size)]

arr_sorted = generate_sorted_array(750)

##arr_sorted = [1, 2, 3, 4, 5]
start = time.time()
print("Array with sorted elements:", heapsort(arr_sorted))
det_time = time.time() - start
print(f"Heapsort Time: {det_time:.5f} seconds")





# Edge Case 5: Reverse sorted array
def generate_reverse_sorted_array(size, start_value=500, step=1):
    # Generate a reverse sorted array with `size` elements, starting from `start_value` and decreasing by `step`
    return [start_value - i * step for i in range(size)]

arr_reverse_sorted = generate_reverse_sorted_array(750)

##arr_reverse_sorted = [5, 4, 3, 2, 1]
start = time.time()
print("Array with Reverse sorted elements:", heapsort(arr_reverse_sorted))
det_time = time.time() - start
print(f"Heapsort Time: {det_time:.5f} seconds")





# Edge Case 6: Random array
def generate_random_unsorted_array(size, min_value=1, max_value=1000):
    # Generate an array with `size` elements, values between `min_value` and `max_value`
    return [random.randint(min_value, max_value) for _ in range(size)]

arr_random = generate_random_unsorted_array(750)
##print(arr_random)

start = time.time()
print("Random Array:", heapsort(arr_random))
det_time = time.time() - start
print(f"Heapsort Time: {det_time:.5f} seconds")