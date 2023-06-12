# Testing Python sort algorithms against algorithms written by ChatGPT
from datetime import datetime
import numpy as np
from enum import Enum
import pprint

startTime = datetime.now()
print("\nStarted script at: {}".format(startTime))
print("\n* * * * BEGIN CODE EXECUTION * * * *\n")

### CODE EXEC START

class Sorting_Type(Enum):
    NP_SORT = 1
    CHATGPT_QUICK_SORT = 2

def init_array_i32(N):
    arr = np.random.randint(0, 2**31-1, size=N, dtype=np.int32)
    return arr

def np_sort(arr):
    np.sort(arr)

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

orders_of_magnitude = 6

execution_time_dict = {
    Sorting_Type.NP_SORT: {},
    Sorting_Type.CHATGPT_QUICK_SORT: {},
}

print(execution_time_dict)

for i in range(1, orders_of_magnitude + 1):
    elms = 10**i
    print("Sorting 10^{} <i64> elements ({})\n. . . . . . . .".format(i, f'{elms:,}'))

    #np sort
    arr = init_array_i32(elms)
    startTime = datetime.now()
    np_sort(arr)
    endTime = datetime.now()
    execution_time_dict[Sorting_Type.NP_SORT].update({elms: str(endTime - startTime)})

    #chatgpt sort
    arr = init_array_i32(elms)
    startTime = datetime.now()
    chatgpt_quick_sort(arr, 0, len(arr) - 1)
    endTime = datetime.now()
    execution_time_dict[Sorting_Type.CHATGPT_QUICK_SORT].update({elms: str(endTime - startTime)})

    #new line formatting
    print()

# Print results
pprint.pprint(execution_time_dict)

### CODE EXEC END

endTime = datetime.now()
print("\n* * * *  END  CODE EXECUTION * * * *\n")
print("Ended script at: {}".format(endTime))
print("Script execution time: {}\n".format(endTime - startTime))