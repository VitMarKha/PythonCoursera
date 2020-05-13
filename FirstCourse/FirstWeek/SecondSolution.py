import sys

size = int(sys.argv[1])
step = 0

size_probel = size - 1
size_simbol = size - (size - 1)

while (step < size) and (size_probel != 0) and (size_simbol != size):
    print(" " * size_probel, end="")
    print("#" * size_simbol)
    size_probel -= 1
    size_simbol += 1
    step += 1
print("#" * size, end="")
