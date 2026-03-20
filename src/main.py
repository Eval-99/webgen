import os
import shutil

from copy_recur import copy_recur


def main():
    if os.path.exists("public"):
        shutil.rmtree("public")

    copy_recur(os.path.join(os.getcwd(), "static"), os.path.join(os.getcwd(), "public"))


if __name__ == "__main__":
    main()
