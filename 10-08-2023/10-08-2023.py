import itertools

def calculate_average_divisible_by_seven(number_str):
    # Generate all permutations of the digits
    permutations = list(itertools.permutations(number_str))

    # Check each permutation for divisibility by 7
    divisible_permutations = []
    for permutation in permutations:
        permutation_value = int(''.join(permutation))
        if permutation_value % 7 == 0:
            divisible_permutations.append(permutation_value)

    if divisible_permutations:
        # Calculate the average between the smallest and largest divisible permutations
        average = (min(divisible_permutations) + max(divisible_permutations)) / 2
        return average
    else:
        return None

number_str = "1867"
average = calculate_average_divisible_by_seven(number_str)

if average:
    print("Average:", average)
else:
    print("No divisible permutations found.")
