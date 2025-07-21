#Linear_search
def linear_search(lst, target):
    for index in range(len(lst)):
        if lst[index] == target:
            return index
    return -1
numbers = list(map(int, input("enter numbers seperated by space:").split()))
x = int(input("enter the number to search for:"))

result = linear_search(numbers, x)
if result != -1:
    print(f"{x} found at index {result}.")
else:
    print(f"{x} not found in the list.")

#Bubble sort 
def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j +1] = lst[j + 1], lst[j]
    return lst
numbers = list(map(int, input("enter numbers to sort (space seperated):").split()))
sorted_list = bubble_sort(numbers)
print("sorted list:", sorted_list)

#Fibonacci sequence
def fibonacci(n):
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence
terms = int(input("enter the number of fibonacci terms: "))
print(f"fibonacci sequence ({terms} terms):", fibonacci(terms))

#Factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1 
    return n * factorial(n - 1)
num = int(input("enter a number to calculate its factorial:"))
print(f"factorial of {num} is:", factorial(num))
