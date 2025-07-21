name = input("enter a word to reverse")
def reverse_string(s):
    return s[::-1]
print("reversed:",reverse_string(name))

def is_prime(n):
    if n <=1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

num = int(input("enter a number to check if its prime:"))
if is_prime(num):
    print(num, "is a prime number.")
else:
    print(num, "is not a prime number.")

def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
num = int(input("enter anumber to find its factorial:"))
print("factorial of", num, "is:", factorial(num))

def find_max(lst):
    max_num = lst[0]
    for num in lst:
        if num > max_num:
            max_num = num
    return max_num

try:
    numbers = input("Enter numbers separated by spaces: ")
    num_list = list(map(int, numbers.split()))
    print("The maximum number is:", find_max(num_list))
except ValueError:
    print("Error: Please enter only numbers separated by spaces.")
except IndexError:
    print("Error: You didn't enter any numbers.")

def is_palindrome(s):
    return s == s[::-1]
text = input("enter a word to check if its a palindrome:")

if is_palindrome(text):
    print(f"'{text}'is a palindrome.")
else:
    print(f"'{text}'is not a palindrome.")    

