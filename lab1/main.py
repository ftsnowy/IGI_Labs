import calculator


print("HELLO WORLD!")
print("Enter A:")
a = int(input())
print("Enter B:")
b = int(input())
print("Enter operator:")
operator = input()
print("Result:", calculator.calculate(a, b, operator))
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = []
for i in range(len(numbers)):
    if numbers[i] % 2 == 0:
        even_numbers.append(numbers[i])
print("Even numbers from list:", even_numbers)
