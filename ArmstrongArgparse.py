import argparse

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

# define the parser
parser = argparse.ArgumentParser(description='Program to calculate Armstrong numbers and their sum.')
parser.add_argument('start', type=int, help='Starting number for the range')
parser.add_argument('end', type=int, help='Ending number for the range')

# parse the arguments
args = parser.parse_args()

# extract the arguments
start_number = args.start
end_number = args.end

# calculate Armstrong numbers and their sum
armstrong_numbers = []
for number in range(start_number, end_number+1):
    if is_armstrong(number):
        armstrong_numbers.append(number)

print(f"Armstrong numbers between {start_number} and {end_number}:")
for number in armstrong_numbers:
    print(number)

sum_of_armstrong_numbers = recursive_sum(armstrong_numbers)

print(f"Sum of Armstrong numbers between {start_number} and {end_number}: {sum_of_armstrong_numbers}")
