import re
from functools import reduce

def sum_mult_matches(matches):
    matches_multiplied = [int(operators[0])*int(operators[1]) for operators in matches]
    return reduce(lambda accum, curr: accum + curr, matches_multiplied)

# Extract data from file
data = None
with open("./data.txt", "r") as file:
    data = file.read()

# Find matches v1
expression_v1 = r"mul\((\d{1,3}),(\d{1,3})\)"
matches_v1 = re.findall(expression_v1, data)
sum_matches_multiplied_v1 = sum_mult_matches(matches_v1)

# Find matches v2
expression_v2 = r"don't\(\).*?do\(\)"
processed_data = re.sub(expression_v2, "", data, flags=re.S)
matches_v2 = re.findall(expression_v1, processed_data)
sum_matches_multiplied_v2 = sum_mult_matches(matches_v2)

# Results
print("Result 1:")
print(sum_matches_multiplied_v1)
print("Result 2:")
print(sum_matches_multiplied_v2)