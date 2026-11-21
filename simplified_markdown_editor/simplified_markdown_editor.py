FORMATTERS = [
    "plain",
    "bold",
    "italic",
    "header",
    "link",
    "inline-code",
    "ordered-list",
    "unordered-list",
    "new-line",
]

SPECIAL_COMMANDS = ["!help", "!done"]


def print_help():
    print(f"Available formatters: {' '.join(FORMATTERS)}")
    print(f"Special commands: {' '.join(SPECIAL_COMMANDS)}")


def format_plain() -> str:
    text = input("Text: > ")
    return text


def format_bold() -> str:
    text = input("Text: > ")
    return f"**{text}**"


def format_italic() -> str:
    text = input("Text: > ")
    return f"*{text}*"


def format_inline_code() -> str:
    text = input("Text: > ")
    return f"`{text}`"


def format_new_line() -> str:
    return "\n"


def format_header() -> str:
    while True:
        try:
            level = int(input("Level: > "))
        except ValueError:
            print("The level should be within the range of 1 to 6.")
            continue

        if 1 <= level <= 6:
            text = input("Text: > ")
            return f"{'#' * level} {text}\n"
        else:
            print("The level should be within the range of 1 to 6.")


def format_link() -> str:
    label = input("Label: > ")
    url = input("URL: > ")
    return f"[{label}]({url})"


def format_list(ordered: bool) -> str:
    while True:
        try:
            rows = int(input("Number of rows: > "))
        except ValueError:
            print("The number of rows should be greater than zero")
            continue

        if rows > 0:
            items = []
            for i in range(1, rows + 1):
                row_text = input(f"Row #{i}: > ")
                if ordered:
                    items.append(f"{i}. {row_text}")
                else:
                    items.append(f"* {row_text}")
            return "\n".join(items) + "\n"
        else:
            print("The number of rows should be greater than zero")


FORMATTER_HANDLERS = {
    "plain": format_plain,
    "bold": format_bold,
    "italic": format_italic,
    "header": format_header,
    "link": format_link,
    "inline-code": format_inline_code,
    "ordered-list": lambda: format_list(ordered=True),
    "unordered-list": lambda: format_list(ordered=False),
    "new-line": format_new_line,
}


def save_output(content: str, filename: str = "output.md"):
    with open(filename, "w", encoding="utf-8") as file:
        file.write(content)


def main():
    markdown_parts = []

    while True:
        choice = input("Choose a formatter: > ").strip()

        if choice == "!help":
            print_help()
            continue

        if choice == "!done":
            save_output("".join(markdown_parts), "output.md")
            break

        if choice not in FORMATTER_HANDLERS:
            print("Unknown formatting type or command")
            continue

        formatted = FORMATTER_HANDLERS[choice]()
        markdown_parts.append(formatted)
        print("".join(markdown_parts), end="" if formatted.endswith("\n") else "\n")


if __name__ == "__main__":
    main()