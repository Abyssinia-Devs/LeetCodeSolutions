print("Number Analyzer")

Input = list(map(int, input("Enter numbers separated by space: ").split()))

even_count = 0
odd_count = 0
even_numbers = []
odd_numbers = []

for i in Input:
    if i % 2 == 0:
        even_count += 1
        even_numbers.append(i)
    else:
        odd_count += 1
        odd_numbers.append(i)

print("Total numbers:", len(Input))
print("Even count:", even_count)
print("Even numbers:", even_numbers)
print("Odd count:", odd_count)
print("Odd numbers:", odd_numbers)
print("Smallest number:", min(Input))
print("Largest number:", max(Input))
