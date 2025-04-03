def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def main():
    try:
        num = int(input("Nhập vào một số nguyên dương: "))
        if num <= 0:
            print("Vui lòng nhập một số nguyên dương.")
        else:
            if is_prime(num):
                print(f"{num} là số nguyên tố.")
            else:
                print(f"{num} không phải là số nguyên tố.")
    except ValueError:
        print("Vui lòng nhập một số nguyên hợp lệ.")

if __name__ == "__main__":
    main()
