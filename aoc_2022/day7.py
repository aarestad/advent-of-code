from dataclasses import dataclass
from typing import Dict
import re


@dataclass
class File:
    name: str
    size: int


class Directory:
    def __init__(self, name):
        self.name = name
        self.files = {}
        self.subdirs = {}

    def __str__(self):
        return self.__recursive_str()

    def dir_size(self):
        size = 0

        for f in self.files.values():
            size += f.size

        for subdir in self.subdirs.values():
            size += subdir.dir_size()

        return size

    def __recursive_str(self, indent=0):
        ret = f"name={self.name} files={sum(f.size for f in self.files.values())} total size={self.dir_size()}"
        if self.dir_size() <= 100_000:
            ret += " *"
        for subdir in self.subdirs.values():
            indent_spaces = " " * indent
            ret += f"\n{indent_spaces}subdir:{subdir.__recursive_str(indent+2)}"

        return ret


root = Directory("/")


def get_dir_from_path(path: list[str], current_dir: Directory = root):
    if not len(path) or not path[0]:
        return current_dir

    return get_dir_from_path(path[1:], current_dir.subdirs[path[0]])


def calculate_dir_size_under_100k(
    current_dir: Directory = root, total_under_100k: int = 0
):
    current_dir_size = current_dir.dir_size()

    if current_dir_size < 100_000:
        total_under_100k += current_dir.dir_size()

    for subdir in current_dir.subdirs.values():
        total_under_100k += calculate_dir_size_under_100k(subdir)

    return total_under_100k


if __name__ == "__main__":
    example = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""

    example_input = example.split("\n")

    with open("input/day7.txt") as input:
        problem_input = [i.strip() for i in input.readlines()]

    current_dir_name = ""
    current_dir = root

    for line in problem_input:
        if line.startswith("$"):
            split_cmd = line[2:].split()  # skip initial "$ "

            if split_cmd[0] == "cd":
                target = split_cmd[1]

                if re.match("[a-z]+", target):
                    current_dir_name += f"/{target}"
                elif target == "..":
                    parts = current_dir_name.split("/")
                    current_dir_name = "/".join(current_dir_name.split("/")[:-1])
                else:  # should only be "/"
                    current_dir_name = ""
            elif split_cmd[0] == "ls":
                current_dir = get_dir_from_path(current_dir_name.split("/")[1:])
        else:
            (size_or_type, name) = line.split()

            if size_or_type == "dir":
                # print(f"adding directory {name} to {current_dir.name}")
                current_dir.subdirs[name] = Directory(name)
            else:
                # print( f"adding file {name} of size {size_or_type} to {current_dir.name}")
                current_dir.files[name] = File(name, int(size_or_type))

    print(root)
    print(calculate_dir_size_under_100k())
