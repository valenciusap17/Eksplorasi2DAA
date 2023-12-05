import random
import math

# Creating dataset of 10 element
num = random.randrange(50, 100, 2)
sum = num / 2

# Generating first list
target = sum
first = [0] * 5
for i in range(4):
    new = random.randint(1, math.floor(target / 2))
    first[i] = new
    target -= new

first[4] = int(target)

# Generating second list
target = sum
second = [0] * 5
for i in range(4):
    new = random.randint(1, math.floor(target / 2))
    second[i] = new
    target -= new

second[4] = int(target)

third = first + second
random.shuffle(third)

# write to txt
with open("tenElementDataset.txt", "w") as f:
    for i in third:
        f.write(str(i))
        f.write("\n")


# Creating dataset of 40 element
num = random.randrange(250, 300, 2)
sum = num / 2
print(sum)
# Generating first list
target = sum
first = [0] * 20
for i in range(19):
    new = random.randint(1, math.floor(target / 4))
    first[i] = new
    target -= new

first[19] = int(target)

# Generating second list
target = sum
second = [0] * 20
for i in range(19):
    new = random.randint(1, math.floor(target / 4))
    second[i] = new
    target -= new

second[19] = int(target)
third = first + second
random.shuffle(third)

# write to txt
with open("fortyElementDataset.txt", "w") as f:
    for i in third:
        f.write(str(i))
        f.write("\n")
        
        
# Creating dataset of 80 element
num = random.randrange(800, 1000, 2)
sum = num / 2
print(sum)
# Generating first list
target = sum
first = [0] * 40
for i in range(39):
    new = random.randint(1, math.floor(target / 8))
    first[i] = new
    target -= new

first[39] = int(target)

# Generating second list
target = sum
second = [0] * 40
for i in range(39):
    new = random.randint(1, math.floor(target / 8))
    second[i] = new
    target -= new

second[39] = int(target)

third = first + second
random.shuffle(third)

# write to txt
with open("eightyElementDataset.txt", "w") as f:
    for i in third:
        f.write(str(i))
        f.write("\n")
