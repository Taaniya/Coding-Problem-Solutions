#!/bin/env python

def max_heapify(arr, n, i):
    l = 2*i + 1
    r = 2*i + 2
    largest = i
    if (l < n) and (arr[l] > arr[i]):
        largest = l
    else:
        largest = i
    if (r < n) and (arr[r] > arr[largest]):
        largest = r
    if i!= largest:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, n, largest)

def heapSort(arr):
    n = len(arr)

    # build max heap
    for i in range(int(n/2)-1, -1, -1):
        max_heapify(arr, n, i)
    
    # Extract max value
    for size in range(n, 0, -1 ):
       # swap the largest value with the last element in the array
        arr[size-1] , arr[0] = arr[0] , arr[size-1]
        max_heapify(arr, size-1,0)

    return arr
    
if __name__ == "__main__":
    arr = [3, 8, 2, 4]
    sorted_arr = heapSort(arr)
    print(sorted_arr)
    
