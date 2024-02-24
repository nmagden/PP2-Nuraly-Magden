#ex1
def generate_squares(N):
    for i in range(N):
        yield i **2
        
try:
    N = int(input("Enter a number (N) to generate squares up to N: "))
    square_generator = generate_squares(N)
    print("Generated squares: ")
    for square in square_generator:
        print(square)
except ValueError:
        print("Invalid input")
        
#ex2
def even_generator(n):
    for i in range(0, n + 1, 2):
        yield i

def main():
    try:
        n = int(input("Enter the value of n: "))
        if n < 0:
            print("Please enter a non-negative integer.")
            return

        even_numbers = even_generator(n)
        result = ",".join(map(str, even_numbers))
        print(f"Even numbers between 0 and {n}: {result}")

    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()

#ex3
def generate(n):
    for i in range(n + 1):
            if i % 3 == 0 and i % 4 == 0:
                yield i
                
n = int(input("Enter a number (n): "))
print("Numbers between 0 and {n} divisible by both 4 and 3 : ")
for num in generate(n):
    print(num)
#ex4
def squares(a, b):
    for i in range(a, b + 1 ):
        yield i ** 2
        
a = int(input("Enter the starting number (a): "))
b = int(input("Enter the ending number (b): "))
print("Squares from {a} to {b} ")
for square in squares(a, b):
    print(square)
#ex5
def generate(n):
    while n >= 0:
        yield n
        n -= 1
n = int(input("Enter a number(n): "))
print("Counting down from {n} to 0 :")
for number in generate(n):
    print(number)
    
        