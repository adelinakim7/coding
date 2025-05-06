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

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def insertion_sort(arr, left, right):
    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1
        while j >= left and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def merge(left, mid, right, arr):
    left_temp = arr[left:mid + 1]
    right_temp = arr[mid + 1:right + 1]

    i = 0
    j = 0
    k = left

    while i < len(left_temp) and j < len(right_temp):
        if left_temp[i] <= right_temp[j]:
            arr[k] = left_temp[i]
            i += 1
        else:
            arr[k] = right_temp[j]
            j += 1
        k += 1

    while i < len(left_temp):
        arr[k] = left_temp[i]
        i += 1
        k += 1

    while j < len(right_temp):
        arr[k] = right_temp[j]
        j += 1
        k += 1

def tim_sort(arr):
    min_run = 32
    n = len(arr)

    for start in range(0, n, min_run):
        end = min(start + min_run - 1, n - 1)
        insertion_sort(arr, start, end)

    size = min_run
    while size < n:
        for left in range(0, n, size * 2):
            mid = min(n - 1, left + size - 1)
            right = min((left + 2 * size - 1), (n - 1))

            if mid < right:
                merge(left, mid, right, arr)
        size *= 2

    return arr

if __name__ == "__main__":
    original_list_bubble = [27, 55, 177, 69, 444, 52, 37]
    print("Список до сортировки пузырьком:", original_list_bubble)

    sorted_list_bubble = bubble_sort(original_list_bubble.copy())
    print("Список после сортировки пузырьком:", sorted_list_bubble)

    original_list_tim = [27, 55, 177, 69, 444, 52, 37]
    print("\nСписок до сортировки Тимсорт:", original_list_tim)

    sorted_list_tim = tim_sort(original_list_tim.copy())
    print("Список после сортировки Тимсорт:", sorted_list_tim)
