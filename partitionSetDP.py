import time
import tracemalloc


def findPartition(arr, n):
    sum = 0
    i, j = 0, 0

    # calculate sum of all elements
    for i in range(n):
        sum += arr[i]

    if sum % 2 != 0:
        return False

    part = [[True for i in range(n + 1)] for j in range(sum // 2 + 1)]

    # initialize top row as true
    for i in range(0, n + 1):
        part[0][i] = True

    # initialize leftmost column,
    # except part[0][0], as 0
    for i in range(1, sum // 2 + 1):
        part[i][0] = False

    # fill the partition table in
    # bottom up manner
    for i in range(1, sum // 2 + 1):
        for j in range(1, n + 1):
            part[i][j] = part[i][j - 1]

            if i >= arr[j - 1]:
                part[i][j] = part[i][j] or part[i - arr[j - 1]][j - 1]

    return part[sum // 2][n]


# Driver code
arr = [1, 3, 3, 2, 3, 2]
n = len(arr)

# Function call
if findPartition(arr, n) == 1:
    print("Can be divided into two subsets of equal sum")
else:
    print("Can not be divided into two subsets of equal sum")


def execute_partition(filename, n):
    with open(filename, "r") as f:
        inputs = [int(line.strip()) for line in f]
    tracemalloc.start()
    start_time = time.time()
    result = findPartition(inputs, n)
    # write to txt
    with open(f"{n}ElementDatasetOutputDP.txt", "w") as f:
        f.write(f"Output for dataset with {n} elements\n")
        f.write(
            "Running time: %s in milliseconds\n" % ((time.time() - start_time) * 1000)
        )
        current, peak = tracemalloc.get_traced_memory()
        f.write(f"Memory usage: Current={current}, Peak={peak}\n")
        if result:
            f.write("Can be divided into two subsets of equal sum\n")
        else:
            f.write("Can not be divided into two subsets of equal sum\n")
    f.close()


execute_partition("tenElementDataset.txt", 10)
execute_partition("fortyElementDataset.txt", 40)
execute_partition("eightyElementDataset.txt", 80)
