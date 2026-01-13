def get_mode() -> str:
    mode = input("1 — перезаписать, 2 — добавить: ").strip()
    return "w" if mode == "1" else "a"


def read_lines_from_user() -> list[str]:
    print("\nВведите текст (пустая строка — конец):")
    lines = []
    while True:
        s = input()
        if s == "":
            break
        lines.append(s)
    return lines


def write_user_input(path: str = "user_input.txt") -> None:
    mode = get_mode()
    lines = read_lines_from_user()
    with open(path, mode, encoding="utf-8") as f:
        f.write("\n".join(lines) + ("\n" if lines else ""))


if __name__ == "__main__":
    write_user_input()



