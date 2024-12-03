import re


def main():
    print(do_mul_and_sum(parse_file("input.txt")))


def mul(AB: tuple[str, str]) -> int:
    pass


def parse_file(path: str) -> list[str]:
    with open(path, "r") as file:
        file_content = " ".join(file.read().split("\n"))
        valid_opperations = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", file_content)
        print(valid_opperations)
        return valid_opperations


def do_mul_and_sum(ops: list[str]) -> int:
    total: int = 0
    for op in ops:
        total += mul(op)
    return total


if __name__ == "__main__":
    main()
