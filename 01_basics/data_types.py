if __name__ == '__main__':
    n = int(input())
    if n < 1 or n > 150:
        print("Input is out of bounds")
    else:
        for i in range(n):
            print(i+1, end="")