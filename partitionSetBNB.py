import tracemalloc
import time


def findPartition(
    values,
    start_index,
    total_value,
    unassigned_value,
    test_assignment,
    test_value,
    best_assignment,
    best_err,
):
    # Convert the best assignment list to be mutable inside the function
    best_assignment["value"] = list(best_assignment["value"])

    # If start_index is beyond the end of the array, then all entries have been assigned.
    if start_index >= len(values):
        # We're done. See if this assignment is better than what we have so far.
        test_err = abs(2 * test_value - total_value)
        if test_err < best_err["value"]:
            # This is an improvement. Save it.
            best_err["value"] = test_err
            best_assignment["value"] = test_assignment.copy()
            print(best_err["value"])
    else:
        # See if there's any way we can assign the remaining items to improve the solution.
        test_err = abs(2 * test_value - total_value)
        if test_err - unassigned_value < best_err["value"]:
            # There's a chance we can make an improvement.
            # We will now assign the next item.
            unassigned_value -= values[start_index]

            # Try adding values[start_index] to set 1.
            test_assignment[start_index] = True
            findPartition(
                values,
                start_index + 1,
                total_value,
                unassigned_value,
                test_assignment,
                test_value + values[start_index],
                best_assignment,
                best_err,
            )

            # Try adding values[start_index] to set 2.
            test_assignment[start_index] = False
            findPartition(
                values,
                start_index + 1,
                total_value,
                unassigned_value,
                test_assignment,
                test_value,
                best_assignment,
                best_err,
            )


# Example usage


def execute_partition(filename, n):
    with open(filename, "r") as f:
        inputs = [int(line.strip()) for line in f]
    tracemalloc.start()
    start_time = time.time()
    # inputs = [9, 2, 4, 3, 4, 10, 14, 10, 7, 1]  # Sample array
    total_value = sum(inputs)
    unassigned_value = total_value
    test_assignment = [False] * len(inputs)
    best_assignment = {"value": [False] * len(inputs)}
    best_assignment = list(best_assignment["value"])
    best_err = {"value": float("inf")}
    findPartition(
        inputs,
        0,
        total_value,
        unassigned_value,
        test_assignment,
        0,
        best_assignment,
        best_err,
    )

    with open(f"{n}ElementDatasetOutputBNB.txt", "w") as f:
        f.write(
            f"Running time: %s in milliseconds \n" % ((time.time() - start_time) * 1000)
        )
        current, peak = tracemalloc.get_traced_memory()
        f.write(f"Memory usage: Current={current}, Peak={peak}\n")
        f.write(
            f"Best Assignment: {best_assignment['value']}\n",
        )
        f.write(f"Best Error: {best_err['value']}\n")


execute_partition("tenElementDataset.txt", 10)
execute_partition("fortyElementDataset.txt", 40)
execute_partition("eightyElementDataset.txt", 80)
