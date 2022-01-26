import os
import sys
from os.path import isfile, join

"""
import os

old_file_name = "/home/career_karma/raw_data.csv"
new_file_name = "/home/career_karma/old_data.csv"

os.rename(old_file_name, new_file_name)

print("File renamed!")
"""


"""
Lib needs to be install for converting HEIF to JPG
sudo add-apt-repository ppa:strukturag/libheif
sudo apt-get install libheif-examples
sudo apt-get update
"""


def get_all_files(dir_path):
    file_paths = []
    for f in os.listdir(dir_path):
        fpath = join(dir_path, f)
        if isfile(fpath):
            file_paths.append(fpath)

    return file_paths


def get_all_jpg_files(file_paths):
    return [fp for fp in file_paths if fp.endswith(".JPG")]


def remove_mov_files(dir_path):
    all_files = get_all_files(dir_path)
    jpg_files = get_all_jpg_files(all_files)
    for f in jpg_files:
        mov_f = f[:-4] + ".MOV"
        if mov_f in all_files:
            print(f"\nfound   : {f}")
            print(f"deleting: {mov_f}")
            os.remove(mov_f)
            print("Done")

        mov_f_lower = f[:-4] + ".mov"
        if mov_f_lower in all_files:
            print(f"\nfound   : {f}")
            print(f"deleting: {mov_f_lower}")
            os.remove(mov_f_lower)
            print("Done")


def main(dir_path):
    remove_mov_files(dir_path)


if __name__ == "__main__":
    if sys.argv[1]:
        main(sys.argv[1])


