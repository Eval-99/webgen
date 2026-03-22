import os
import shutil

from copy_recur import copy_recur
from page_gen import generate_pages_recursive


def main():
    if os.path.exists("public"):
        shutil.rmtree("public")

    copy_recur(os.path.join(os.getcwd(), "static"), os.path.join(os.getcwd(), "public"))
    generate_pages_recursive("content", "template.html", "public")


if __name__ == "__main__":
    main()
