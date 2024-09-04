def fibonacci(n):
    a, b = 0, 1
    seq = []

    for i in range(n):
        seq.append(a)
        a, b = b, a + b

    return seq

def main():
    n = int(input("Enter the number: ")) 
    
    if n <= 0:
        print("Please enter a positive integer.")
    else:
        print(f"The first {n} numbers in the Fibonacci sequence are: {fibonacci(n)}")

if __name__ == "__main__":
    main()
