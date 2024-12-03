def main():
    vals: list[list[int]] = parse_input("input.txt")
    return get_num_safe_rows(vals)


def parse_input(path: str) -> list[list[int]]:
    out: list[list[int]] = []
    with open(path, "r") as file:
        for row in file:
            parsed_row: list[int] = row.split(" ")
            parsed_row = [int(x) for x in parsed_row]
            out.append(parsed_row)

    return out


def is_row_mostly_safe(array: list[int]) -> bool:
    for element in array:
        temp: list[int] = array[:]
        temp.remove(element)
        if is_row_safe(temp):
            return True

    return is_row_safe(array)


def is_row_safe(array: list[int]) -> bool:
    diffs: list[int] = []
    for idx in range(len(array)):
        try:
            diffs.append(array[idx] - array[idx + 1])
        except IndexError:
            break
    positive = None
    for val in diffs:
        if abs(val) < 1 or abs(val) > 3:
            return False
        if positive is None:
            positive = True if abs(val) == val else False

        if not (abs(val) == val) == positive:
            return False

    return True


def get_num_safe_rows(array: list[list[int]]) -> int:
    safe_count: int = 0
    for row in array:
        if is_row_mostly_safe(row):
            safe_count += 1

    return safe_count


if __name__ == "__main__":
    print(main())
