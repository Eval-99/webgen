import os
import shutil
import sys

from copy_recur import copy_recur
from page_gen import generate_pages_recursive


def main():
    try:
        basepath = sys.argv[1]
    except IndexError:
        basepath = "/"

    if os.path.exists("docs"):
        shutil.rmtree("docs")

    copy_recur(os.path.join(os.getcwd(), "static"), os.path.join(os.getcwd(), "docs"))
    generate_pages_recursive("content", "template.html", "docs", basepath)


if __name__ == "__main__":
    main()
