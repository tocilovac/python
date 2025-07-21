def primes_in_range(start, end):
    primes = []
    for num in range(start, end + 1):
        if num < 2:
            continue  # Skip numbers less than 2 (not primes)
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):  # Check divisors up to sqrt(num)
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes

start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))
print(f"Prime numbers between {start} and {end} are:", primes_in_range(start, end))



def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count  # Corrected: Moved outside the loop

text = input("Enter a sentence or word: ")
print("Number of vowels:", count_vowels(text)) 


def is_anagram(str1, str2):
    return sorted(str1.lower()) == sorted(str2.lower())
word1 = input("enter the first word:")
word2 = input("enter the second word:")
if is_anagram(word1, word2):
    print(f"'{word1}' and '{word2}' are anagrams.")
else:
    print(f"'{word1}' and '{word2}' are not anagrams.")


def fibonacci(n):
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence
terms = int(input("enter the number of fibonacci terms: "))
print(f"fibonacci sequence ({terms} terms):", fibonacci(terms))
  
