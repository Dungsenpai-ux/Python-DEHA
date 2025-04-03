def bubble_sort(arr):
    n = len(arr)
    swapped = True
    while swapped:
        swapped = False
        for i in range(1, n):
            if arr[i-1] > arr[i]:
                arr[i-1], arr[i] = arr[i], arr[i-1]
                swapped = True
        n -= 1

arr = list(map(int, input("Nhập vào một mảng số nguyên, cách nhau bởi dấu cách: ").split()))
bubble_sort(arr)
print("Mảng sau khi sắp xếp tăng dần:", arr)
