from collections import Counter


def main():
    destinations: list[list[int]] = take_input("input.txt")
    return get_list_dist(destinations), get_list_similarity(destinations)


def take_input(path: str) -> list[list[int]]:
    out: list[list[int]] = [[], []]
    with open(path, "r") as file:
        for line in file:
            parts: list[str] = line.split(" ", 1)
            out[0].append(int(parts[0].strip()))
            out[1].append(int(parts[1].strip()))
            out[0].sort()
            out[1].sort()
    return out


def get_list_dist(array: list[list[int]]) -> int:
    dist: int = 0
    for pair in zip(array[0], array[1]):
        dist += abs(pair[0] - pair[1])

    return dist


def get_list_similarity(array: list[list[int]]) -> int:
    total: int = 0
    for num in array[0]:
        total += num * array[1].count(num)

    return total


if __name__ == "__main__":
    print(main())
