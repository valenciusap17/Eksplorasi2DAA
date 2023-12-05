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
    if start_index >= len(values):
        # base case
        test_err = abs(2 * test_value - total_value)
        if test_err < best_err[0]:
            best_err[0] = test_err
            best_assignment[:] = test_assignment[:]
            print(best_err[0])
    else:
        # Check if there is a chance to improvement
        test_err = abs(2 * test_value - total_value)
        if test_err - unassigned_value < best_err[0]:
            # There is a possiblity
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


def execute_partition(filename, n):
    with open(filename, "r") as f:
        inputs = [int(line.strip()) for line in f]
    total_value = sum(inputs)
    unassigned_value = total_value
    test_assignment = [False] * len(inputs)
    best_assignment = [False] * len(inputs)
    best_err = [float("inf")]
    start_time = time.time()
    tracemalloc.start()
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
    current, peak = tracemalloc.get_traced_memory()

    with open(f"{n}ElementDatasetOutputBNB.txt", "w") as f:
        f.write(
            f"Running time: %s in milliseconds \n" % ((time.time() - start_time) * 1000)
        )
        f.write(f"Memory usage: Current={current}, Peak={peak}\n")
        f.write(
            f"Best Assignment: {best_assignment}\n",
        )
        f.write(f"Best Error: {best_err[0]}\n")


execute_partition("tenElementDataset.txt", 10)
# execute_partition("fortyElementDataset.txt", 40)
# execute_partition("eightyElementDataset.txt", 80)
