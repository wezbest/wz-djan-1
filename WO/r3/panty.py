from src.fun import m1, m2
from rich.traceback import install
from rich import print as rprint

install(show_locals=True)


def main():
    m1()  # Markup Funtion
    m2()  # Server Run Function


if __name__ == "__main__":
    main()
