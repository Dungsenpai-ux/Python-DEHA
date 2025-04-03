def factorial(n):
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def main():
    try:
        num = int(input("Nhập vào một số nguyên không âm: "))
        if num < 0:
            print("Vui lòng nhập một số nguyên không âm.")
        else:
            print(f"Giai thừa của {num} là {factorial(num)}.")
    except ValueError:
        print("Vui lòng nhập một số nguyên hợp lệ.")

if __name__ == "__main__":
    main()
