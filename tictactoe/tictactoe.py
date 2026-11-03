def print_board(cells):
    print("-" * 9)
    for i in range(3):
        row = cells[i * 3:(i + 1) * 3]
        print(f"| {row[0]} {row[1]} {row[2]} |")
    print("-" * 9)


def analyze_game(cells):
    x_count = cells.count('X')
    o_count = cells.count('O')

    if abs(x_count - o_count) >= 2:
        return "Impossible"

    def check_win(player):
        win_coords = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ]
        for coord in win_coords:
            if cells[coord[0]] == player and cells[coord[1]] == player and cells[coord[2]] == player:
                return True
        return False

    x_wins = check_win('X')
    o_wins = check_win('O')

    if x_wins and o_wins:
        return "Impossible"

    if x_wins:
        return "X wins"
    if o_wins:
        return "0 wins"

    has_empty = '_' in cells or ' ' in cells
    if not has_empty:
        return "Draw"

    return "Game not finished"


def get_player_move(cells, current_player):
    while True:
        raw_input_data = input("Enter the coordinates: ")
        parts = raw_input_data.split()

        if len(parts) != 2 or not parts[0].isdigit() or not parts[1].isdigit():
            print("You should enter numbers!")
            continue

        r, c = int(parts[0]), int(parts[1])

        if not (1 <= r <= 3 and 1 <= c <= 3):
            print("Coordinates should be from 1 to 3!")
            continue

        index = (r - 1) * 3 + (c - 1)

        if cells[index] != '_' and cells[index] != ' ':
            print("This cell is occupied! Choose another one!")
            continue

        return index


def main():
    cells = ['_'] * 9
    current_player = 'X'

    print_board(cells)

    while True:
        index = get_player_move(cells, current_player)
        cells[index] = current_player
        print_board(cells)

        status = analyze_game(cells)

        if status == "X wins":
            print("X wins")
            break
        elif status == "0 wins":
            print("0 wins")
            break
        elif status == "Draw":
            print("Draw")
            break
        elif status == "Impossible":
            print("Impossible")
            break
        elif status == "Game not finished":
            current_player = 'O' if current_player == 'X' else 'X'


if __name__ == "__main__":
    main()