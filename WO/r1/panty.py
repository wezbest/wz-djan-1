# Django testing

from src.utils import label1
import django


def main():
    label1("Printing Django Version")
    print(django.get_version())


if __name__ == "__main__":
    main()
