from src.fun import markdown1, run_server
from rich.traceback import install

install(show_locals=True)


def main():
    markdown1()  # Initial Mardown
    run_server()  # Run server


if __name__ == "__main__":
    main()
