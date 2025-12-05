from pathlib import Path


def part1(input_file):
    with open(input_file, "r") as f:
        data = [line.strip() for line in f.readlines()]

        dial_position = 50
        dial_max = 100
        password = 0

        for rotate in data:
            match rotate[0]:
                case "L":
                    dial_position = (
                        dial_position - int(rotate[1:]) + dial_max
                    ) % dial_max
                case "R":
                    dial_position = (dial_position + int(rotate[1:])) % dial_max
                case x:
                    raise ValueError(f"Unknown rotate ({x})")
            if dial_position == 0:
                password += 1

        print(password)


def part2(input_file):
    with open(input_file, "r") as f:
        data = [line.strip() for line in f.readlines()]

        dial_position = 50
        dial_max = 100
        password = 0

        for rotate in data:
            value = int(rotate[1:])
            if value >= dial_max:
                password += value // dial_max
                value %= dial_max
            match rotate[0]:
                case "L":
                    new_dial_position = dial_position - value
                    if new_dial_position <= 0 and dial_position != 0:
                        password += 1
                case "R":
                    new_dial_position = dial_position + value
                    if new_dial_position >= dial_max:
                        password += 1
                case x:
                    raise ValueError(f"Unknown rotate ({x})")
            dial_position = (new_dial_position + dial_max) % dial_max

        print(password)


if __name__ == "__main__":
    input_file = Path(__file__).parent / "input.txt"
    part1(input_file)
    part2(input_file)
