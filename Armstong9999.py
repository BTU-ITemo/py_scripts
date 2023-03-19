# recursive function to calculate the sum of a list of numbers
def recursive_sum(numbers):
    if len(numbers) == 1:
        return numbers[0]
    else:
        return numbers[0] + recursive_sum(numbers[1:])

# function to check if a number is an Armstrong number
def is_armstrong(number):
    n = len(str(number))
    total = sum([int(digit)**n for digit in str(number)])
    return total == number

armstrong_numbers = []

for number in range(9, 10000):
    if is_armstrong(number):
        armstrong_numbers.append(number)
        
print("Armstrong numbers between 9 and 9999:")
for number in armstrong_numbers:
    print(number)

sum_of_armstrong_numbers = recursive_sum(armstrong_numbers)

print("Sum of Armstrong numbers between 9 and 9999:", sum_of_armstrong_numbers)
