def get_number_of_pencils():
    while True:
        pencils_input = input("How many pencils would you like to use:\n> ")
        if not pencils_input.isdigit():
            print("The number of pencils should be numeric")
            continue

        pencils = int(pencils_input)
        if pencils <= 0:
            print("The number of pencils should be positive")
            continue

        return pencils


def get_first_player(name1, name2):
    while True:
        first_input = input(f"Who will be the first ({name1}, {name2}):\n> ")
        if first_input not in [name1, name2]:
            print(f"Choose between '{name1}' and '{name2}'")
            continue
        return first_input


def get_bot_move(pencils_count):
    remainder = pencils_count % 4
    if remainder == 0:
        return 3
    elif remainder == 3:
        return 2
    elif remainder == 2:
        return 1
    else:
        return 1


def get_player_move(current_player, pencils_count):
    while True:
        move_input = input(f"{current_player}'s turn:\n> ")
        if not move_input.isdigit():
            print("Possible values: '1', '2' or '3'")
            continue

        move = int(move_input)
        if move not in [1, 2, 3]:
            print("Possible values: '1', '2' or '3'")
            continue

        if move > pencils_count:
            print("Too many pencils were taken")
            continue

        return move


def main():
    name1 = "John"
    name2 = "Jack"

    pencils = get_number_of_pencils()
    first_player = get_first_player(name1, name2)

    current_player = first_player

    while pencils > 0:
        print("|" * pencils)

        if current_player == name2:
            move = get_bot_move(pencils)
            print(f"{name2}'s turn:")
            print(move)
        else:
            move = get_player_move(current_player, pencils)

        pencils -= move

        if pencils == 0:
            winner = name2 if current_player == name1 else name1
            print(f"{winner} won!")
            break

        current_player = name2 if current_player == name1 else name1


if __name__ == "__main__":
    main()