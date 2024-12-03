import re


def calculate(instructions):
    multiplications = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", instructions)
    return sum(
        int(multiplication[0]) * int(multiplication[1])
        for multiplication in multiplications
    )


with open("input.txt") as file:
    instructions = " ".join(file.read().split("\n"))

print(calculate(instructions))
instructions = re.sub(r"don't\(\).+?do\(\)", "", instructions)
print(calculate(instructions))
