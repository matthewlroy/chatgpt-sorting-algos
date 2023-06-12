# Testing Python sort algorithms against algorithms written by ChatGPT
from datetime import datetime
import numpy as np
from enum import Enum
import pprint
import random
import matplotlib.pyplot as plt

startTime = datetime.now()
print("\nStarted script at: {}".format(startTime))
print("\n* * * * BEGIN CODE EXECUTION * * * *\n")

### CODE EXEC START

class Sorting_Type(Enum):
    NP_SORT = 1
    CHATGPT_QUICK_SORT = 2
    CHATGPT_QUICK_SORT_RANDOM_PIVOT = 3
    CHATGPT_OPTIMAL_SORT = 4
    CHATGPT_QUICK_SORT_2 = 5

def init_array_i32(N):
    arr = np.random.randint(0, 2**31-1, size=N, dtype=np.int32)
    return arr

def np_sort(arr):
    np.sort(arr)

# PROMPT: Create a sorting algorithm for an extremely large array of int32s
def chatgpt_quick_sort(arr, low, high):
    if low < high:
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        pi = i + 1
        chatgpt_quick_sort(arr, low, pi - 1)
        chatgpt_quick_sort(arr, pi + 1, high)

# PROMPT: Enhance your previous (chatgpt_quick_sort) function to be more optimal
def chatgpt_quick_sort_randomized_pivot(arr, low, high):
    if low < high:
        pivot_index = random.randint(low, high)
        arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        pi = i + 1
        chatgpt_quick_sort_randomized_pivot(arr, low, pi - 1)
        chatgpt_quick_sort_randomized_pivot(arr, pi + 1, high)

# PROMPT: The sort you made is still 3 orders of mangitude slower than numpys sort. optimzie it more
def chatgpt_optimal_sort(arr, low, high):
    if low < high:
        # Use Insertion Sort for small arrays
        if high - low + 1 < 10:
            for i in range(low + 1, high + 1):
                key = arr[i]
                j = i - 1
                while j >= low and arr[j] > key:
                    arr[j + 1] = arr[j]
                    j -= 1
                arr[j + 1] = key
            return
        
        # Use QuickSort for larger arrays
        pivot_index = random.randint(low, high)
        arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        pi = i + 1
        chatgpt_optimal_sort(arr, low, pi - 1)
        chatgpt_optimal_sort(arr, pi + 1, high)

# PROMPT: The 'chatgpt_optimal_sort()' function you wrote is still much slower than numpy's built-in sort. 
# Try copying what numpy does for sorting to improve performance. You cannot use any built-in sorting 
# methods provided by Python or numpy.
def chatgpt_quicksort_2(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return chatgpt_quicksort_2(left) + middle + chatgpt_quicksort_2(right)

orders_of_magnitude = 6

execution_time_dict = {
    Sorting_Type.NP_SORT: {},
    Sorting_Type.CHATGPT_QUICK_SORT: {},
    Sorting_Type.CHATGPT_QUICK_SORT_RANDOM_PIVOT: {},
    Sorting_Type.CHATGPT_OPTIMAL_SORT: {},
    Sorting_Type.CHATGPT_QUICK_SORT_2: {},
}

print(execution_time_dict)

for i in range(1, orders_of_magnitude + 1):
    elms = 10**i
    print("\nSorting 10^{} <i64> elements ({})\n. . . . . . . .".format(i, f'{elms:,}'))

    #np sort
    arr = init_array_i32(elms)
    startTime = datetime.now()
    np_sort(arr)
    endTime = datetime.now()
    execution_time_dict[Sorting_Type.NP_SORT].update({elms: endTime - startTime})

    #chatgpt quick sort
    arr = init_array_i32(elms)
    startTime = datetime.now()
    chatgpt_quick_sort(arr, 0, len(arr) - 1)
    endTime = datetime.now()
    execution_time_dict[Sorting_Type.CHATGPT_QUICK_SORT].update({elms: endTime - startTime})

    #chatgpt sort pivot
    arr = init_array_i32(elms)
    startTime = datetime.now()
    chatgpt_quick_sort_randomized_pivot(arr, 0, len(arr) - 1)
    endTime = datetime.now()
    execution_time_dict[Sorting_Type.CHATGPT_QUICK_SORT_RANDOM_PIVOT].update({elms: endTime - startTime})

    #chatgpt sort optimal
    arr = init_array_i32(elms)
    startTime = datetime.now()
    chatgpt_optimal_sort(arr, 0, len(arr) - 1)
    endTime = datetime.now()
    execution_time_dict[Sorting_Type.CHATGPT_OPTIMAL_SORT].update({elms: endTime - startTime})

    #chatgpt quick sort 2
    arr = init_array_i32(elms)
    startTime = datetime.now()
    chatgpt_quicksort_2(arr)
    endTime = datetime.now()
    execution_time_dict[Sorting_Type.CHATGPT_QUICK_SORT_2].update({elms: endTime - startTime})


    #new line formatting
    print()

### CODE EXEC END

endTime = datetime.now()
print("\n* * * *  END  CODE EXECUTION * * * *\n")
print("Ended script at: {}".format(endTime))
print("Script execution time: {}\n".format(endTime - startTime))

# Print results
pprint.pprint(execution_time_dict)

# Plot results
# Convert the time deltas to seconds
for sort_type in execution_time_dict:
    for size in execution_time_dict[sort_type]:
        time_delta = execution_time_dict[sort_type][size]
        seconds = time_delta.total_seconds()
        execution_time_dict[sort_type][size] = seconds

# Create the plot
for sort_type in execution_time_dict:
    sizes = list(execution_time_dict[sort_type].keys())
    times = list(execution_time_dict[sort_type].values())
    plt.plot(sizes, times, label=str(sort_type))

# Add labels and legend
plt.xlabel('Input Size')
plt.ylabel('Time (seconds)')
plt.title('Sorting Algorithm Performance')
plt.legend()

# Show the plot
plt.show()