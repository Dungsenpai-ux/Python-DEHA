#đảo ngược mảng số
# def reverse_array(arr):
#     return arr[::-1]
#
# # Ví dụ sử dụng
# numbers = [1, 2, 3, 4, 5]
# reversed_numbers = reverse_array(numbers)
# print("Mảng ban đầu:", numbers)
# print("Mảng sau khi đảo ngược:", reversed_numbers)

#tìm số lớn nhất
# def reverse_array(arr):
#     return arr[::-1]
#
# def find_max(arr):
#     return max(arr) if arr else None
#
# # Ví dụ sử dụng
# numbers = [1, 2, 3, 4, 5]
# reversed_numbers = reverse_array(numbers)
# max_number = find_max(numbers)
#
# print("Mảng ban đầu:", numbers)
# print("Mảng sau khi đảo ngược:", reversed_numbers)
# print("Số lớn nhất trong mảng:", max_number)

#
def reverse_array(arr):
    return arr[::-1]

def find_max(arr):
    return max(arr) if arr else None

def find_second_max(arr):
    unique_arr = list(set(arr))
    if len(unique_arr) < 2:
        return None
    unique_arr.remove(max(unique_arr))
    return max(unique_arr)

def remove_duplicates(arr):
    return list(set(arr))

# Ví dụ sử dụng
numbers = [1, 2, 3, 4, 5, 3, 2, 1]
numbers = remove_duplicates(numbers)
reversed_numbers = reverse_array(numbers)
max_number = find_max(numbers)
second_max_number = find_second_max(numbers)

print("Mảng sau khi xóa phần tử trùng lặp:", numbers)
print("Mảng sau khi đảo ngược:", reversed_numbers)
print("Số lớn nhất trong mảng:", max_number)
print("Số lớn thứ hai trong mảng:", second_max_number)

