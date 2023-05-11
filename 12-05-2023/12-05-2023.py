def min_task_cost(efficiency):
    efficiency.sort()  # Sort efficiencies in ascending order
    min_cost = float('inf')  # Initialize minimum cost as infinity

    # Iterate through each worker to be excluded
    for i in range(len(efficiency)):
        cost = 0
        pair_idx = 0

        # Iterate through the remaining workers in adjacent pairs
        while pair_idx < len(efficiency) - 2:
            pair_cost = abs(efficiency[pair_idx] - efficiency[pair_idx + 1])
            cost += pair_cost
            pair_idx += 2

        # Update minimum cost if the current cost is lower
        min_cost = min(min_cost, cost)

        # Rotate the list by excluding the current worker
        efficiency = efficiency[1:] + [efficiency[0]]

    return min_cost

efficiency = [1, 3, 54, 712, 52, 904, 113, 12, 135, 32, 31, 56, 23, 79, 611, 123, 677, 232, 997, 101, 111,
123, 2, 7, 24, 57, 99, 45, 666, 42, 104, 129, 554, 335, 876, 35, 15, 93, 13]
print(min_task_cost(efficiency))
