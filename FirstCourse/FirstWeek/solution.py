import sys

digit_string = sys.argv[1]
result = 0

for step in digit_string:
    result += int(step)
print(result)
