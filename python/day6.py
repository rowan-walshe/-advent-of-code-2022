INPUT = 'day6-input.txt'

PACKET_HEADER_LENGTH = 4
MESSAGE_HEADER_LENGTH = 14


def sequence_start(stream: str, size: int) -> int:
    # Return the index of the first character after n consecutively different characters
    for i in range(size, len(stream)):
        header = stream[i-size:i]
        if len(set(header)) == size:
            return i
    raise Exception("Couldn't find packet header")


if __name__ == '__main__':
    with open(INPUT, 'r') as f:
        line = f.readline()

    # Part 1 - Find the index after 4 consecutive different characters
    print(f'Part 1: {sequence_start(line, PACKET_HEADER_LENGTH)}')

    # Part 2 -Find the index after 14 consecutive different characters
    print(f'Part 2: {sequence_start(line, MESSAGE_HEADER_LENGTH)}')