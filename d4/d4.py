import re
import numpy as np


PATTERN = r'\d+'


with open('assert.txt') as f:
    raw = f.read()
    bingo_subsystem = [x for x in raw.split('\n\n')]
    numbers = [int(x) for x in bingo_subsystem[0].split(',')]
    boards = np.array([np.array(re.findall(PATTERN, x), dtype=int).reshape(5, 5)
                       for x in bingo_subsystem[1:]])


def winning_board(numbers, boards):
    for n in numbers:
        hits = np.where(boards == n)
        boards[hits] = -1
        rows = boards.sum(1)
        columns = boards.sum(2)
        winning_row = np.where(rows == -5)
        winning_column = np.where(columns == -5)
        if all(map(len, winning_row)):
            board_id = winning_row[0]
            unmarked = boards[board_id] != -1
            return boards[board_id][unmarked].sum() * n
        if all(map(len, winning_column)):
            board_id = winning_column[0]
            unmarked = boards[board_id] != -1
            return boards[board_id][unmarked].sum() * n


def last_winning_board(numbers, boards):
    won = set()
    for n in numbers:
        hits = np.where(boards == n)
        boards[hits] = -1
        rows = boards.sum(1)
        columns = boards.sum(2)
        winning_row = np.where(rows == -5)
        winning_column = np.where(columns == -5)
        if all(map(len, winning_row)):
            winning_boards = winning_row[0]
            for board_id in winning_boards:
                won.add(board_id)
                if len(won) == len(boards):
                    unmarked = boards[board_id] != -1
                    return boards[board_id][unmarked].sum() * n
        if all(map(len, winning_column)):
            winning_boards = winning_column[0]
            for board_id in winning_boards:
                won.add(board_id)
                if len(won) == len(boards):
                    unmarked = boards[board_id] != -1
                    return boards[board_id][unmarked].sum() * n


assert winning_board(numbers, boards) == 4512
assert last_winning_board(numbers, boards) == 1924


with open('input.txt') as f:
    raw = f.read()
    bingo_subsystem = [x for x in raw.split('\n\n')]
    numbers = [int(x) for x in bingo_subsystem[0].split(',')]
    boards = np.array([np.array(re.findall(PATTERN, x), dtype=int).reshape(5, 5)
                       for x in bingo_subsystem[1:]])


print(winning_board(numbers, boards))
print(last_winning_board(numbers, boards))
