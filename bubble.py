def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
numbers = [27, 77, 444, 52, 67]
print("Исходный список чисел:", numbers)
sorted_numbers = buble_sort(numbers)
print("отсортированный массив: ", sorted_numbers)
