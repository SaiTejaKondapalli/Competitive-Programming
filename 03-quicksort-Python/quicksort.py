"""Implement quick sort in Python.
Input a list.
Output a sorted list."""


def qsort(arr, low, high):
	if low < high:
		p = partition(arr, low, high)
		qsort(arr, low, p - 1)
		qsort(arr, p + 1, high)

def partition(arr, low, high):
	i = low - 1
	pivot = arr[high]
	for j in range(low, high):
		if arr[j] < pivot:
			i += 1
			arr[i], arr[j] = arr[j], arr[i]
	arr[i + 1], arr[high] = arr[high], arr[i + 1]
	return i + 1

def quicksort(array):
	# Your code goes here
	qsort(array, 0, len(array) - 1)
	return array