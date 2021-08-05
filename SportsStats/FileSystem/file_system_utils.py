import os
from SportsStats.settings import *


def try_make_dir(name) -> None:
    """
    This function tries to make a directory with a provided name.
    If the directory already exists, just use the existing directory.
    :param name:
    :return:
    """
    try:
        os.mkdir(name)
    except OSError:
        print(f"Directory '{name}' already exists; using this existing directory.")


def get_dir_files(path) -> list:
    files = []
    contents = os.listdir(path)
    for item in contents:
        item = LINKS_DIR + "/" + item
        if os.path.isfile(item):
            files.append(item)
    return files


def append(path, content) -> None:
    with open(path, "a") as f:
        f.write(content)


def write(path, content) -> None:
    with open(path, "w") as f:
        f.write(content)


def del_file_content(path) -> None:
    write(path, "")


def read(path) -> str:
    with open(path, "r") as f:
        return f.read()


def init_data_dir():
    try_make_dir(DATA_DIR)
    try_make_dir(ALL_PLAYERS_DIR)
    try_make_dir(LINKS_DIR)
