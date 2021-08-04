import os
import json
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


def smart_write(path, content) -> None:
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


def read_json(path) -> dict:
    with open(path, "r") as f:
        return json.load(f)


def write_json(path, new_content) -> None:
    with open(path, "a") as f:
        json.dump(new_content, f, indent=4)


def reset_json_file(path) -> None:
    del_file_content(path)
    write(path, "{}")
