def make_example_txt(path="example.txt"):
    try:
        open(path, "r", encoding="utf-8").close()
    except FileNotFoundError:
        with open(path, "w", encoding="utf-8") as f:
            f.write("Первая строка\nВторая строка\nТретья строка\nЧетвёртая строка\n")
def read_file(path="example.txt", mode="all", n=10):
    with open(path, "r", encoding="utf-8") as f:
        if mode == "all":
            print(f.read())
        elif mode == "lines":
            with open(path, "r", encoding="utf-8") as file:
                for i, line in enumerate(file, 1):
                    print(f"{i}: {line.rstrip()}")
        elif mode == "size":
            with open(path, "r", encoding="utf-8") as file:
                chunk = file.read(n)
                while chunk:
                    print(chunk)
                    chunk = file.read(n)
        else:
            print("mode: all | lines | size")

if __name__ == "__main__":
    make_example_txt()
    read_file(mode="all")
    print()
    read_file(mode="lines")
    print()
    read_file(mode="size", n=15)